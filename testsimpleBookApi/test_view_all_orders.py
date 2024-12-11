import requests

from utils.myconfigparser import getPetApiURL
from utils.myutils import *
import logging

logger = logging.getLogger(__name__)

baseURI = getPetApiURL()
path = '/orders/'


# view the all orders with authentication
def test0012_View_AllOrder(get_token):
    token = get_token
    url = baseURI + path
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = getApiData(url, headers)
    print(data)
    assert resp_status == 200
    assert 'orderId' in data


# view the all orders without  authentication
def test0013_View_AllOrder(get_token):
    token = 'invalid token'
    url = baseURI + path
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = getApiData(url, headers)
    print(data)
    assert resp_status == 401
    assert 'orderId' not in data
