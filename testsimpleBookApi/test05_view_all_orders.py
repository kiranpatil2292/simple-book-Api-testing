import requests

from utils.myconfigparser import getPetApiURL
from utils.myutils import *
import logging
logger=logging.getLogger(__name__)

baseURI = getPetApiURL()
path = '/orders/'


# view the all orders with authentication
def test0012_View_SingleOrder(get_token):
    token = get_token
    url = baseURI + path
    data, resp_status, timeTaken = getApiData(url)
    print(data)


# view the all orders without  authentication
def test0013_View_SingleOrder(get_token):
    token = get_token
    url = baseURI + path
    data, resp_status, timeTaken = getApiData(url)
    print(data)
