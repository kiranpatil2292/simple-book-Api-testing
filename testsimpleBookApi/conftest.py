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


@pytest.fixture(scope='session')
def get_token():
    loginurl = baseURI + loginURLPath
    #payload = getjsonFromFile(LoginJsonFile)
    payload = {"clientName": fake.name(), "clientEmail": fake.email()}
    headers = {'content-Type': 'application/json'}
    resp = postApidata(loginurl, payload, headers)

    # print(resp.json()['token'])
    token = resp.json().get("accessToken")
    if not token:
        raise ValueError("Access token not found in the response JSON")

    yield token  # Provide the token to tests

    # Teardown: Cleanup actions after all tests using the fixture
    revoke_url = baseURI + "/logout"
    revoke_headers = {'Authorization': f"Bearer {token}"}
    revoke_resp = requests.post(revoke_url, headers=revoke_headers)
    if revoke_resp.status_code == 200:
        print("Token successfully revoked.")
    else:
        print(f"Failed to revoke token. Status code: {revoke_resp.status_code}, Response: {revoke_resp.text}")
