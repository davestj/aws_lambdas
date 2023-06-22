# EC2 AMI Copy Script

This script allows you to copy an EC2 AMI from one AWS account to another, while encrypting the volumes and using a customer managed KMS key.

## Prerequisites

- Python 3
- `boto3` library

## Usage

1. Install the required dependencies by running the following command:
   ```bash
   pip install boto3
   ```

2. Replace the placeholder values in the script:
   - Replace `'ami-12345678'` with your source AMI ID.
   - Replace `'arn:aws:kms:us-east-1:123456789012:key/abcd1234-5678-90ab-cdef-1234567890ab'` with your KMS key ARN.

3. Execute the script using the following command:
   ```bash
   python ami_copy_script.py <source_region> <destination_region> <destination_account_id>
   ```
   Make sure to provide the necessary command line arguments:
   - `<source_region>`: The region where the source AMI is located.
   - `<destination_region>`: The region where you want to copy the AMI.
   - `<destination_account_id>`: The AWS account ID where you want to copy the AMI.

## Example

To copy an AMI from `us-west-2` to `eu-west-1` in the AWS account with ID `123456789012`, you would run the following command:
```bash
python ami_copy_script.py us-west-2 eu-west-1 123456789012
```

## License

This script is licensed under the [GPL V3](LICENSE.md).
