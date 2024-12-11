import requests

from utils.myutils import postApidata, getApiData
from utils.myconfigparser import getPetApiURL
import pytest
import logging
logger = logging.getLogger(__name__)
import random
from faker import Faker
fake = Faker()
registerJsonfile = 'registerApiValid.json'
baseURI = getPetApiURL()
order = '/orders'


# place order with token
# @pytest.mark.parametrize("customer_id, customer_name", [ (7, "john"), (8, "rajesh")])

# def test007_PlaceOrder(get_token, customer_id, customer_name):
@pytest.fixture()
def place_order(get_token):
    token = get_token
    url = baseURI + '/orders'
    # payload = {"id": customer_id, "customerName": customer_name}
    payload = {"bookId": 1, "customerName": fake.name()}
    headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()  # Ensure the request succeeded
    print(resp.text)
    order_id = resp.json().get("orderId")
    if not order_id:
        raise ValueError(f"Order ID not found in response: {resp.json()}")

    return order_id


# # place order without token
def test008_PlaceOrder(get_token,place_order):
    token = get_token
    print(token)
    url = baseURI + order
    payload = {"bookId": random.randint(1,20), "customerName": fake.name()}
    headers = {"content-Type": "application/json"}
    data, resp_status, timeTaken = postApidata(url, payload, headers)
    logger.info('placing order without token')
    print(data)
    assert data["error"] == 'Missing Authorization header.'
    assert resp_status == 401


# place order with wrong playload data & order with token
def test009_PlaceOrder(get_token):
    token = get_token
    print(token)
    url = baseURI + order
    payload = {"bookId": random.uniform(10.0, 20.0), "customerName": fake.name()}
    headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = postApidata(url, payload, headers)
    logger.info('placeing order with invalid user with token')
    print(data)
   
    assert resp_status != 201


def test0010_View_SingleOrder(place_order, get_token):
    orderid = place_order
    token = get_token
    print(orderid)
    url = baseURI + f'/orders/{orderid}'
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = getApiData(url, headers)

    assert resp_status == 200
    assert data.get("id") == orderid
