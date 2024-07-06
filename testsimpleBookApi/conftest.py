import pytest
from utils.fileutils import getjsonFromFile
from utils.myconfigparser import getPetApiURL
from utils.apiutils import PostApidata

LoginJsonFile = 'registerApiValid.json'
baseURI = getPetApiURL()
loginURLPath = '/api-clients'


@pytest.fixture(scope='session')
def get_token():
    loginurl = baseURI + loginURLPath
    payload = getjsonFromFile(LoginJsonFile)
    headers = {'content-Type': 'application/json'}
    resp = PostApidata(loginurl, payload,headers)

    # print(resp.json()['token'])
    token = resp.json().get("accessToken")
    if not token:
        raise ValueError("Access token not found in the response JSON")

    return token

