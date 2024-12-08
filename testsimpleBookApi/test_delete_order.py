from utils.myconfigparser import getPetApiURL
from utils.apiutils import *
import logging
import random
logger = logging.getLogger(__name__)
from faker import Faker

fake = Faker()
baseURI = getPetApiURL()


# delete order with invalid orderid
def test0017_delete_order(get_token):
    token = get_token
    orderid = '1smsdmw'
    url = baseURI + f'orders/:{orderid}'
    payload = {'customerName': fake.name()}
    headers = {"content-Type": "application/json", "Authorization": f"bearer{token}"}
    data, resp_status, timeTaken = deletedata(url, headers)
    logger.info('delete order with invalid orderid')
    print(data)
    assert resp_status == 404


# delete order with valid orderid
def test0018_delete_order(get_token, place_order):
    token = get_token
    orderid = place_order
    url = baseURI + f"orders/:{orderid}"
    headers = {"content-Type": "application/json", "Authorization": f"bearer{token}"}
    data, resp_status, timeTaken = deletedata(url, headers)
    logger.info('delete order with valid orderid is initiated')
    assert resp_status==204
    print(data)


# delete order with payload
def test0019_delete_order(get_token, place_order):
    token = get_token
    orderid = place_order
    url = baseURI + f"orders/:{orderid}"
    payload = {'customerName': fake.name()}
    headers = {"content-Type": "application/json", "Authorization": f"bearer{token}"}
    data, resp_status, timeTaken = requests.delete(url, json=payload, headers=headers)
    logger.info('delete order with payload is initiated')
    print(data)
    assert resp_status == 400
