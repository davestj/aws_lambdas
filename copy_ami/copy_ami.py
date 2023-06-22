import boto3
import sys


def copy_ami(source_region, destination_region, destination_account_id):
    source_ami_id = 'ami-12345678'  # Replace with your source AMI ID
    kms_key_id = 'arn:aws:kms:us-east-1:123456789012:key/abcd1234-5678-90ab-cdef-1234567890ab'  # Replace with your KMS key ARN

    # Create AWS clients for source and destination regions
    source_ec2 = boto3.client('ec2', region_name=source_region)
    destination_ec2 = boto3.client('ec2', region_name=destination_region)

    # Get source AMI details
    response = source_ec2.describe_images(ImageIds=[source_ami_id])
    source_ami = response['Images'][0]

    # Copy source AMI to destination account/region
    response = destination_ec2.copy_image(
        SourceImageId=source_ami_id,
        SourceRegion=source_region,
        Encrypted=True,
        KmsKeyId=kms_key_id,
        Name=source_ami['Name'],
        Description=source_ami['Description'],
        DestinationRegion=destination_region,
        DestinationAccountId=destination_account_id
    )

    print("Copied AMI ID:", response['ImageId'])


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python ami_copy_script.py <source_region> <destination_region> <destination_account_id>")
        sys.exit(1)

    source_region = sys.argv[1]
    destination_region = sys.argv[2]
    destination_account_id = sys.argv[3]

    copy_ami(source_region, destination_region, destination_account_id)
