# DevOps ToolSmiths AWS Lambda Suite

## EC2 AMI Copy Script

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
   python copy_ami.py <source_region> <destination_region> <destination_account_id>
   ```
   Make sure to provide the necessary command line arguments:
   - `<source_region>`: The region where the source AMI is located.
   - `<destination_region>`: The region where you want to copy the AMI.
   - `<destination_account_id>`: The AWS account ID where you want to copy the AMI.

## Example

To copy an AMI from `us-west-2` to `eu-west-1` in the AWS account with ID `123456789012`, you would run the following command:
```bash
python copy_ami.py us-west-2 eu-west-1 123456789012
```

## License

This script is licensed under the [GPL V3](LICENSE.md).
# Lambda Function: Hosted Zone Expiration Checker

This Lambda function checks the expiration date of all hosted zones in AWS Route 53 using WHOIS data. It sends an expiration notice email if the domain is expired or within 3 days of expiration.

## Prerequisites

- An AWS account with sufficient permissions to create and configure Lambda functions.
- Python 3.x installed on your local machine.
- AWS Command Line Interface (CLI) installed and configured with your AWS credentials.

## Setup Instructions

### 1. Create the Lambda Function

1. Open your terminal or command prompt.
2. Create a new directory for the Lambda function:

   ```shell
   mkdir hosted-zone-expiration-checker
   cd hosted-zone-expiration-checker
   ```

3. Create a new Python file and paste the provided Lambda function code into it:

   ```shell
   touch lambda_function.py
   ```

   Open the `lambda_function.py` file and paste the Lambda function code.

4. Save the file.

### 2. Package the Lambda Function

1. In the terminal, install the necessary Python packages:

   ```shell
   pip install whois
   ```

2. Create a deployment package by creating a ZIP archive:

   ```shell
   zip -r function.zip lambda_function.py
   ```

### 3. Create the Lambda Function in AWS

1. In the terminal, run the following AWS CLI command to create the Lambda function:

   ```shell
   aws lambda create-function \
     --function-name hosted-zone-expiration-checker \
     --runtime python3.8 \
     --handler lambda_function.check_hosted_zones_expiration \
     --zip-file fileb://function.zip \
     --role <YOUR_LAMBDA_EXECUTION_ROLE_ARN>
   ```

   Replace `<YOUR_LAMBDA_EXECUTION_ROLE_ARN>` with the ARN of the IAM role that allows Lambda function execution.

2. Once the function is created, note down the function's ARN as you will need it later.

### 4. Configure the Email Settings

1. Open the `lambda_function.py` file in a text editor.

2. Locate the `send_email` function and update the following variables:

   - `sender`: Your email address.
   - `smtp_server`: The SMTP server address for sending emails.
   - `smtp_port`: The SMTP server port number.
   - `smtp_username`: Your SMTP server username.
   - `smtp_password`: Your SMTP server password.

   Update these variables with the appropriate values.

3. Save the file.

### 5. Schedule the Lambda Function Execution

1. Go to the AWS Management Console and open the AWS Lambda service.

2. Find and select the "hosted-zone-expiration-checker" function.

3. Scroll down to the "Designer" section and click on "CloudWatch Events" in the "Add triggers" box.

4. Configure the trigger settings:

   - **Rule**: Create a new rule.
   - **Rule name**: Enter a name for the rule.
   - **Rule description**: Optionally, provide a description for the rule.
   - **Schedule expression**: Enter the cron expression to schedule the function execution. For example, to run the function once every day at 8 AM UTC, use `cron(0 8 * * ? *)`.

5. Click "Add".

### 6. Test the Lambda Function

1. In the Lambda function details page, click on the "Test" button.

2. Create a new test event using the "Hello World" template.

3. Provide a name for the test event

 and click "Create".

4. Click on the "Test" button again to execute the function using the created test event.

   This will test if the function runs successfully and print the output in the execution logs.

### 7. Verify Email Notifications

Ensure that the SMTP server and email settings are properly configured to receive email notifications for expired or expiring domains.

## Conclusion

You have successfully set up the "Hosted Zone Expiration Checker" Lambda function to monitor the expiration date of hosted zones in AWS Route 53. The function will run automatically based on the scheduled expression you defined.

Remember to periodically check the CloudWatch Logs for the Lambda function to monitor the execution and ensure the email notifications are sent correctly.



## Make sure to replace 
`<YOUR_LAMBDA_EXECUTION_ROLE_ARN>` with the actual ARN of your Lambda execution role. Additionally, don't forget to update the email configuration variables in the `send_email` function with your own email and SMTP server details.

Feel free to customize the instructions as per your specific environment and requirements.