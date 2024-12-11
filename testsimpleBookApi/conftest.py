import pytest
import requests
from utils.fileutils import getjsonFromFile
from utils.myconfigparser import getPetApiURL
from utils.apiutils import *
import random
from faker import Faker

fake = Faker()
LoginJsonFile = 'registerApiValid.json'
baseURI = getPetApiURL()
loginURLPath = '/api-clients'

#
# @pytest.fixture(scope='session')
# def get_token():
#     loginurl = baseURI + loginURLPath
#     #payload = getjsonFromFile(LoginJsonFile)
#     payload = {"clientName": fake.name(), "clientEmail": fake.email()}
#     headers = {'content-Type': 'application/json'}
#     resp = postApidata(loginurl, payload, headers)
#
#     # print(resp.json()['token'])
#     token = resp.json().get("accessToken")
#     if not token:
#         raise ValueError("Access token not found in the response JSON")
#
#     yield token  # Provide the token to tests
#
#     # Teardown: Cleanup actions after all tests using the fixture
#     revoke_url = baseURI + "/logout"
#     revoke_headers = {'Authorization': f"Bearer {token}"}
#     revoke_resp = requests.post(revoke_url, headers=revoke_headers)
#     if revoke_resp.status_code == 200:
#         print("Token successfully revoked.")
#     else:
#         print(f"Failed to revoke token. Status code: {revoke_resp.status_code}, Response: {revoke_resp.text}")




@pytest.fixture(scope='session')
def get_token():
    """
    A pytest fixture to authenticate and obtain an access token for API tests.
    The token is revoked after the tests are completed.
    """
    # Construct login URL
    loginurl = baseURI + loginURLPath

    # Prepare the payload with random data
    payload = {"clientName": fake.name(), "clientEmail": fake.email()}
    headers = {'Content-Type': 'application/json'}

    # Send the login request
    try:
        resp = requests.post(loginurl, json=payload, headers=headers)
        resp.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to get access token: {e}")

    # Parse the token from the response
    token = resp.json().get("accessToken")
    if not token:
        raise ValueError(f"Access token not found in response JSON: {resp.json()}")

    # Yield the token for use in tests
    yield token

    # Teardown: Revoke the token after tests
    revoke_url = baseURI + "/logout"
    revoke_headers = {'Authorization': f"Bearer {token}"}

    try:
        revoke_resp = requests.post(revoke_url, headers=revoke_headers)
        if revoke_resp.status_code == 200:
            print("Token successfully revoked.")
        else:
            print(f"Failed to revoke token. Status code: {revoke_resp.status_code}, Response: {revoke_resp.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while revoking the token: {e}")
