from dotenv import load_dotenv
import pytest
import os

def test_username_password():
    load_dotenv()
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    print(username, password)
    print("This is dotenvtest")