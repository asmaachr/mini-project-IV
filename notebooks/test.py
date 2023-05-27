## Python test file for flask to test locally
import requests as r
import pandas as pd
import json


# base_url = 'http://127.0.0.1:5000/' #base url local host

base_url = 'http://ec2-3-137-170-11.us-east-2.compute.amazonaws.com:5000/'
json_data = [
    {
    "Loan_ID" : "LP001002",
    "Gender" : "Male",
    "Married" : "No",
    "Dependents" : "0",
    "Education" : "Graduate",
    "Self_Employed" : "No",
    "ApplicantIncome" : 5849,
    "CoapplicantIncome" : 200,
    "LoanAmount" : 1.0,
    "Loan_Amount_Term" : 360.0,
    "Credit_History" : 1.0,
    "Property_Area" : "Urban"
       }
]




# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_data)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')