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
@pytest.fixture(scope="session")
def place_order(get_token):
    token = get_token
    url = baseURI + '/orders'
    # payload = {"id": customer_id, "customerName": customer_name}
    payload = {"id": random.randint(1, 10), "customerName": fake.name()}
    headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, time_taken = postApidata(url, payload, headers)
    logger.info('placing order with valid user with token')
    # assert resp_status == 201
    orderid = data.get("orderid")
    print(orderid)
    return orderid


# # place order without token
def test008_PlaceOrder(get_token):
    token = get_token
    print(token)
    url = baseURI + order
    payload = {'id': random.randint(1,20), 'customerName': fake.name()}
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
    payload = {'id': random.uniform(10.0, 20.0), 'customerName': fake.name()}
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
    assert data.get("orderId") == orderid
