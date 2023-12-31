import boto3
import re
import sys
import pandas as pd
import datetime

def list_free_linux_amis(name_pattern):
    '''
    :param name_pattern:
    :return:
    '''
    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_images(
        Owners=['aws-marketplace'],
        Filters=[
            {'Name': 'root-device-type', 'Values': ['ebs']},
            {'Name': 'virtualization-type', 'Values': ['hvm']},
            {'Name': 'is-public', 'Values': ['true']},
        ],
    )

    ami_data = []
    regex_pattern = name_pattern

    for image in response['Images']:
        provider = image['OwnerId']
        ami_id = image['ImageId']
        name = image['Name']
        build_date = image['CreationDate']

        # Filter images based on name regex pattern
        if re.search(regex_pattern, name):
            ami_data.append({
                'Provider': provider,
                'AMI ID': ami_id,
                'Name': name,
                'Build Date': build_date
            })

    # Sort results by most recent build date
    ami_data = sorted(ami_data, key=lambda x: x['Build Date'], reverse=True)

    # Save results to a text file
    with open('ami_byname.txt', 'w') as file:
        for ami in ami_data:
            # assign ami['Build Date'] value for the build date of an AMI
            build_date_str = ami['Build Date']

            # Convert the build date string to a datetime object
            build_date = datetime.datetime.strptime(build_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

            # Set our current date
            current_date = datetime.datetime.now()

            # Calculate the time difference between the current date and the build date
            time_difference = current_date - build_date

            # Check if the time difference is greater than 30 days and notify of patch management
            if time_difference.days > 30:
                print("WARNING: AMI > than 30 days. for security requirements, run updates.\n")
                file.write(f"PATCH NOTICE: AMI > than 30 days. for security requirements, run updates.\n")
            else:
                print("AMI is CURRENT!\n")
                file.write(f"AMI SECURITY STATUS: last release was less then 30 days ago, may still need updated.\n")
            print(f"Searching by regex pattern: {regex_pattern}")
            file.write(f"Found AMI with pattern: {regex_pattern}\n")
            file.write(f"Provider: {ami['Provider']}\n")
            print(f"Provider: {ami['Provider']}\n")
            file.write(f"AMI ID: {ami['AMI ID']}\n")
            print(f"AMI ID: {ami['AMI ID']}\n")
            file.write(f"Name: {ami['Name']}\n")
            print(f"Name: {ami['Name']}\n")
            file.write(f"Build Date: {ami['Build Date']}\n")
            print(f"Build Date: {ami['Build Date']}\n")
            file.write("--------------------\n")
            print("#------------------------\n")

    # Generate a spreadsheet report
    df = pd.DataFrame(ami_data)
    df.to_excel('ami_byname_report.xlsx', index=False)

# Specify the name regex pattern as a command-line parameter or use a default value
# name_regex = r'(CentOS|Red Hat|Fedora|Almalinux|Rocky Linux)'

# Uncomment the line below to specify the name regex pattern as a command-line parameter
name_regex = sys.argv[1]

list_free_linux_amis(name_regex)

