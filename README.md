# Testing
Test UI and API file uploads
Please clone the repo:
1. Create virtualenv by typing :  virtualenv -p python3 env
2. pip install -r requirements/common.txt
# Instructions to RUN UI test
Please make you to set email and password into your environment variables

If you are running from command line you can use the following command:
behave -m  ui_test/behave/

If you are running it from a interpreter such as as PyCharm 
Script path would be: FileUpload.feature
Interpreter options : -m behave
Parameters: please set email and password

# Instructions to run API test  
Please pass api key as argument parameter
from root :
python3 api_test/test.py --api_key=<token>
