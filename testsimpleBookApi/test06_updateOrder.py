import requests

from utils.myconfigparser import getPetApiURL

from utils.fileutils import getjsonFromFile
from utils.myutils import *
from utils.apiutils import postapiData, getapiData
# import logging

import pytest

baseURI = getPetApiURL()
path='/orders/:orderid' # pass valid orderid value
path1='/orders/:orderid' # pass Invalid orderid value

# update order with valid orderid
def test0014_update_order(get_token):
    token = get_token
    url = baseURI + path
    payload = { 'customerName': 'abc'}
    headers = {"content-Type": "application/json", "x-access-token": token}
    data, resp_status, timeTaken = putdata(url, payload, headers)
    print(data)

# update order with invalid orderid
def test0015_update_order(get_token):
    token = get_token
    url = baseURI + path
    payload = {'customerName': 'abc'}
    headers = {"content-Type": "application/json", "x-access-token": token}
    data, resp_status, timeTaken = putdata(url, payload, headers)
    print(data)

# update order with invalid payload data
def test0016_update_order(get_token):
    token = get_token
    url = baseURI + path
    payload = {'customerName': 123}
    headers = {"content-Type": "application/json", "x-access-token": token}
    data, resp_status, timeTaken = putdata(url, payload, headers)
    print(data)
