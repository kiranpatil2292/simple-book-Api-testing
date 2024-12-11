from utils.myconfigparser import getPetApiURL
from utils.apiutils import getApiData, postApidata, patchdata
import logging
import random
from faker import Faker

fake = Faker()
import requests

baseURI = getPetApiURL()


# multiple request in a loop
def test_rate_limit():
    url = baseURI
    for i in range(1000):  # Simulate exceeding rate limit
        headers = {'content-Type': 'application/json'}
        response = getApiData(url, headers)
        if response.status_code == 429:
            print("Rate limit exceeded:", response.json())
            break


#  payload  larger than the  server max  limit
def test_larger_payload():
    url = baseURI
    large_payload = {"data": "x" * (10 * 1024 * 1024 + 1)}  # Payload > 10 MB
    headers = {'content-Type': 'application/json'}
    response = postApidata(url, large_payload, headers)

    if response.status_code == 413:
        print("Payload too large:", response.json())

#
# url = "https://api.example.com/upload"
# large_payload = {"data": "x" * (6 * 1024 * 1024 + 1)}  # Payload > 10 MB
# response = requests.post(url, json=large_payload)
#
# if response.status_code == 200:
#     print("File uploaded successfully:", response.json())
