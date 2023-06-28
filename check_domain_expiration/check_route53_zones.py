import argparse
import whois
import boto3
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient):
    '''
    :param subject:
    :param body:
    :param recipient:
    :return:
    '''
    sender = 'your_email@example.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
        print(f"Expiration notice email sent to: {recipient}")
    except Exception as e:
        print(f"Failed to send expiration notice email: {str(e)}")

def check_hosted_zones_expiration(event, context, recipient):
    '''
    :param event:
    :param context:
    :param recipient:
    :return:
    '''
    # Create Route 53 client
    route53 = boto3.client('route53')

    # Get all hosted zones
    response = route53.list_hosted_zones()
    hosted_zones = response['HostedZones']

    for zone in hosted_zones:
        zone_name = zone['Name']
        print(f"Checking expiration date for zone: {zone_name}")

        # Extract domain name from hosted zone
        domain_name = zone_name.rstrip('.')

        try:
            # Perform WHOIS lookup
            w = whois.whois(domain_name)

            # Check if the domain is registered and has an expiration date
            if w.status and w.expiration_date:
                expiration_date = w.expiration_date[0]  # Access the first element of the list

                # Calculate the remaining days until expiration
                days_until_expiration = (expiration_date - datetime.now()).days

                if days_until_expiration <= 0:
                    # Domain is expired
                    subject = f"Domain Expiration Notice: {domain_name}"
                    body = f"The domain {domain_name} has expired."
                    send_email(subject, body, recipient)
                elif days_until_expiration <= 3:
                    # Domain is expiring within 3 days
                    subject = f"Domain Expiration Notice: {domain_name}"
                    body = f"The domain {domain_name} will expire in {days_until_expiration} days."
                    send_email(subject, body, recipient)
                else:
                    print(f"Domain: {domain_name}, Expiration Date: {expiration_date}")

            else:
                print(f"Domain: {domain_name}, Expiration Date: Not Found")

        except Exception as e:
            print(f"Error checking expiration date for domain: {domain_name}")
            print(str(e))

    return {
        'statusCode': 200,
        'body': 'Expiration date check completed'
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check expiration dates of hosted zones')
    parser.add_argument('--recipient', required=True, help='Recipient email address')

    args = parser.parse_args()
    check_hosted_zones_expiration(None, None, args.recipient)
