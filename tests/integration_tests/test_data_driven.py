# Read the Excel or CSV FIle
# Create a function to create_token which can take values from the Excel File
# Validate the Expected Result
import json

import pytest
import openpyxl
import requests

def read_credentials_from_excel(path):
    credentials = []
    #with open("C:\Users\harin\PycharmProjects\APIAutomationGoRest\tests\integration_tests\test_createnewcart.py") as file:
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password = row
        credentials.append({"username":username,"password":password})
    return credentials



def make_request_auth(username,password):
    payload = {
        "username" : username,
        "password" : password
    }
    headers = {
        "Content-Type" : "application/json"
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth",headers=headers,json=payload)
    #assert response.status_code == 200, "Test Failed"
    return response


def test_post_create_token():
    path = r"C:\Users\harin\OneDrive\Desktop\DataFile.xlsx"
    credentials = read_credentials_from_excel(path)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        #print(username,password)
        response = make_request_auth(username,password)
        #print(response)
        vresponse = response.json()
        value = vresponse.values()
        print(value)
        if value == "Bad credentials":
         print("Fail - Not Authenticated")
        else :
         print("Test PASSED")



