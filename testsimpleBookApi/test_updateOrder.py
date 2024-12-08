from utils.myconfigparser import getPetApiURL
from utils.apiutils import *
import logging
logger = logging.getLogger(__name__)
import random
from faker import Faker
fake = Faker()
baseURI = getPetApiURL()


# update order with valid orderid
def test0014_update_order(get_token, place_order):
    token = get_token
    orderid = place_order
    url = baseURI + f'/orders/:{orderid}'
    payload = {'customerName': fake.name()}
    headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = patchdata(url, payload, headers)
    logging.info('update order with valid orderid is started')
    print(data)
    assert resp_status == 200
    assert timeTaken < 4


# update order with invalid orderid
def test0015_update_order(get_token):
    token = get_token
    orderid = 'as123njgh'
    url = baseURI + f'/orders/:{orderid}'
    payload = {'customerName': fake.name()}
    headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = patchdata(url, payload, headers)
    logging.info('update order with invalidId is initiated')
    print(data)
    assert resp_status == 404
    assert timeTaken < 4


# update order with  invalid payload data
def test0016_update_order(get_token, place_order):
    token = get_token
    orderid = place_order
    url = baseURI + f'/orders/:{orderid}'
    payload = {'customerName': random.randint(1, 100)}
    headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = patchdata(url, payload, headers)
    logging.info('update order with invalid payload is initiated')
    print(data)
    assert resp_status == 400
    assert timeTaken < 4
