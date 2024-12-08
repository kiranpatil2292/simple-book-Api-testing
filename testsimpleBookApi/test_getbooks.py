import requests
from utils.myconfigparser import getPetApiURL
from utils.myutils import *
import logging
logger = logging.getLogger(__name__)
baseURI = getPetApiURL()
URLPATH = '/books?type=fiction&limit=10'
URLPATH2 = '/books?type=non-fiction&limit=20'
URLPATH3 = '/books?type=fiction&limit=100'
URLPATH4 = '/books?type=non-fiction&limit=-1'


# verify type of fiction  book within limit

def test001_get_fiction_Books():
    url = baseURI + URLPATH
    headers = {"content-Type": "application/json"}
    data, resp_status, timeTaken = getApiData(url,headers)
    logger.info('verifing fiction books within limit')

    print(data)
    assert data[1]['id'] == 3
    assert data[2]['name'] == 'The Midnight Library'

    assert resp_status == 200
    assert timeTaken <= 4
    print("Time Taken:", timeTaken)


# verify type of non-fiction  book within limit

def test002_get_allNon_Fiction_Books():
    url = baseURI + URLPATH2
    headers = {"content-Type": "application/json"}
    data, resp_status, timeTaken = getApiData(url,headers)
    logger.info('api book validation with non fiction book within limit')
    print(data)
    assert data[0]['id'] == 2
    assert data[1]['name'] == 'Untamed'
    assert resp_status == 200
    assert timeTaken <= 4
    print("Time Taken:", timeTaken)


# verify type of non-fiction  book beyond limit

def test003_get_allNon_Fiction_Books():
    url = baseURI + URLPATH4
    headers = {"content-Type": "application/json"}

    data, resp_status, timeTaken = getApiData(url,headers)
    logger.info('api book validation type of non_fiction beyond limit')
    assert data['error'] == "Invalid value for query parameter 'limit'. Cannot be greater than 20."
    assert resp_status == 400
    assert timeTaken <= 4
    print("Time Taken:", timeTaken)
    print(data)


# verify type of fiction  book beyond limit

def test004_get_all_Fiction_Books():
    url = baseURI + URLPATH3
    headers = {"content-Type": "application/json"}
    data, resp_status, timeTaken = getApiData(url,headers)
    logger.info('api book validation type fiction beyond limit')

    assert data['error'] == "Invalid value for query parameter 'limit'. Cannot be greater than 20."
    assert resp_status == 400
    assert timeTaken <= 4
    print("Time Taken:", timeTaken)
