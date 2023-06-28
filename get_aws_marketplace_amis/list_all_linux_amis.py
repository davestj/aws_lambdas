import boto3
import re
import pandas as pd

def list_free_linux_amis():
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
    regex_pattern = r'(CentOS|Red Hat|Fedora|Almalinux|Rocky)'

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

    # Save results to a text file
    with open('ami_list.txt', 'w') as file:
        for ami in ami_data:
            file.write(f"Provider: {ami['Provider']}\n")
            file.write(f"AMI ID: {ami['AMI ID']}\n")
            file.write(f"Name: {ami['Name']}\n")
            file.write(f"Build Date: {ami['Build Date']}\n")
            file.write("--------------------\n")

    # Generate a spreadsheet report
    df = pd.DataFrame(ami_data)
    df.to_excel('ami_report.xlsx', index=False)

list_free_linux_amis()
