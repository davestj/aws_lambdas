# Script: List Free Linux AMIs

This Python 3 script uses the Boto3 library to list all free Linux AMIs from the AWS Marketplace that are public. 
It filters the AMIs based on a name regex pattern and retrieves information such as the provider, AMI ID, name, and build date. 
It then saves the results to a text file and generates a spreadsheet report.

## Why DevOps Uses This

This script is useful for DevOps teams working with AWS infrastructure. It helps automate the process of finding and managing Linux AMIs by providing a convenient way to filter and extract relevant information. 
DevOps teams often need to deploy infrastructure as code and rely on up-to-date AMIs, and this script helps simplify that process to fork amis for integration.

## Prerequisites

- Python 3 installed
- Boto3 library installed (`pip install boto3`)
- Pandas library installed (`pip install pandas`)

## Usage

1. Ensure you have the required libraries installed.
2. Save the script to a Python file (e.g., `get_linux_amis.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the following command to execute the script:

   ```bash
   python get_linux_amis.py
   ```

   By default, the script uses the regex pattern `(CentOS|Red Hat|Fedora|Almalinux|Rocky Linux)`. You can modify this pattern directly in the script or uncomment the relevant line and specify it as a command-line parameter.
Some example commands using regex to search.
```bash
# Only Get CentOS
python get_linux_amis.py CentOS

#Fetch Fedora Almalinux Rocky based distros
python get_linux_amis.py "Fedora|Almalinux|Rocky Linux"

#Hey Adriene! GO ROCKY!
python get_linux_amis.py "^Rocky.*"

#Only get arm based
get_linux_amis.py "aarch64"
#Look for all that start with Rocky or Alma
python get_linux_amis.py "^Rocky.*|^Alma.*"
```
6. The script will retrieve the AMIs, filter them based on the regex pattern, and save the results to a text file named `ami_list.txt`.
7. It will also generate a spreadsheet report named `ami_report.xlsx` in the same directory.

Note: Make sure your AWS credentials are properly configured before running the script. Refer to the AWS documentation on how to set up your credentials.

