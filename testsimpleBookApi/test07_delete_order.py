import requests

from utils.myconfigparser import getPetApiURL

from utils.fileutils import getjsonFromFile
from utils.myutils import *
from utils.apiutils import postapiData, getapiData
# import logging

import pytest

baseURI = getPetApiURL()
path = '/orders/:orderid'  # pass valid orderid value
path1 = '/orders/:orderid'  # pass Invalid orderid value


# delete order with invalid orderid
def test0017_update_order(get_token):
    token = get_token
    url = baseURI + path
    payload = {'customerName': '123'}
    headers = {"content-Type": "application/json", "x-access-token": token}
    data, resp_status, timeTaken = deletedata(url, payload)
    print(data)


# delete order with valid orderid
def test0018_update_order(get_token):
    token = get_token
    url = baseURI + path
    payload = {'customerName': 'kp'}
    headers = {"content-Type": "application/json", "x-access-token": token}
    data, resp_status, timeTaken = deletedata(url, payload)
    print(data)


# delete order with payload
def test0019_update_order(get_token):
    token = get_token
    url = baseURI + path
    payload = {'customerName': 'dz'}
    headers = {"content-Type": "application/json", "x-access-token": token}
    data, resp_status, timeTaken = deletedata(url, payload)
    print(data)
