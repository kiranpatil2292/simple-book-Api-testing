from utils.myconfigparser import getPetApiURL
from utils.myutils import *
import logging
logger = logging.getLogger(__name__)
# path = '/books/2'
# path2 = '/books/100'
baseURI = getPetApiURL()


# verify to view detail information of book with valid bookid

def test005_getSingleBook():
    url = baseURI + '/books/2'
    headers = {"content-Type": "application/json"}
    data, resp_status, timeTaken = getApiData(url,headers)
    logger.info('api single-book validation with valid bookid')
    print(data)
    assert 'id' in data
    assert data['id'] == 2
    assert data['name'] == 'Just as I Am'
    assert data['author'] == 'Cicely Tyson'
    assert data['type'] == 'non-fiction'
    assert data['price'] == 20.33
    assert data['current-stock'] == 0
    assert data['available'] is False
    assert resp_status == 200
    assert timeTaken <= 4
    print("Time Taken:", timeTaken)


# verify to view detail information of book with invalid bookid

def test006_getSingleBook():
    url = baseURI + '/books/100'
    headers = {"content-Type": "application/json"}
    data, resp_status, timeTaken = getApiData(url,headers)
    print(data)
    logger.info('api single-book validation with invalid bookid')
    assert data['error'] == "No book with id 100"
    assert resp_status == 404
    assert timeTaken <= 2
    print("Time Taken:", timeTaken)
