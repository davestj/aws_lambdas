# Script: List Free Linux AMIs by Name

This Python 3 script utilizes the Boto3 library to retrieve and filter free Linux AMIs from the 
AWS Marketplace based on a provided name pattern. It then saves the filtered results to a text file and 
generates a spreadsheet report.

## Prerequisites

- Python 3 installed
- Boto3 library installed (`pip install boto3`)
- Pandas library installed (`pip install pandas`)

## Usage

1. Open a terminal or command prompt and clone this repo.
2. Navigate to the directory where the script is located.
3. Run the following command to execute the script:

   ```bash
   python list_all_linux_amis.py
   ```

4. The script will connect to AWS using the Boto3 library and retrieve the AMIs.
5. It will save the filtered results to a text file named `ami_byname.txt`, which includes information such as the provider, AMI ID, name, and build date.
6. Additionally, it will generate a spreadsheet report named `ami_byname_report.xlsx` in the same directory.


## Why DevOps Uses This Script

DevOps teams can utilize this script to automate the retrieval and filtering of free Linux AMIs from the AWS Marketplace. It provides the following benefits:

- **Efficiency:** The script automates the process of searching for specific Linux AMIs based on a name pattern, eliminating the need for manual searching and filtering.
- **Consistency:** By using a regular expression pattern, the script ensures consistent and accurate filtering of AMIs based on predefined criteria.
- **Reporting:** The script generates a text file and a spreadsheet report that provide a comprehensive overview of the filtered AMIs, including relevant details such as provider, AMI ID, name, and build date.
- **Customization:** The script can be easily modified to include additional filters or perform additional actions on the retrieved AMI data, allowing for customization based on specific requirements.

The combination of automation, consistency, reporting, and customization makes this script a valuable tool for DevOps teams working with AWS resources.