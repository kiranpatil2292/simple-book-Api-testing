from utils.myutils import postApidata, getApiData
from utils.myconfigparser import getPetApiURL
import pytest
import logging

registerJsonfile = 'registerApiValid.json'
logger = logging.getLogger(__name__)
baseURI = getPetApiURL()
order = '/orders'


# place order with token
# @pytest.mark.parametrize("customer_id, customer_name", [ (7, "john"), (8, "rajesh")])
@pytest.fixture(scope='module')
# def test007_PlaceOrder(get_token, customer_id, customer_name):
def place_order(get_token):
    token = get_token
    url = baseURI + '/orders'
    # payload = {"id": customer_id, "customerName": customer_name}
    payload = {"id": 4, "customerName": "Mamesh"}
    headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, time_taken = postApidata(url, payload, headers)
    logger.info('placing order with valid user with token')
    # assert resp_status == 201
    orderid = data.get("orderid")
    print(orderid)
    return orderid


# # place order without token
# def test008_PlaceOrder(get_token):
#     token = get_token
#     print(token)
#     url = baseURI + order
#     payload = {'id': 6, 'customerName': 'kiran'}
#     headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
#     data, resp_status, timeTaken = postApidata(url, payload, headers)
#     logger.info('placing order without token')
#     print(data)
#     assert data["error"] == 'Missing Authorization header.'
#     assert resp_status == 201
#
#
# # place order with wrong playload data & order with token
# def test009_PlaceOrder(get_token):
#     token = get_token
#     print(token)
#     url = baseURI + order
#     payload = {'id': 7, 'customerName': 'sagar'}
#     headers = {"content-Type": "application/json", "Authorization": f"Bearer {token}"}
#     data, resp_status, timeTaken = postApidata(url, payload, headers)
#     logger.info('placeing order with invalid user with token')
#     print(data)
#     assert data["created"] == 'true'
#     assert resp_status != 201


def test008_PlaceOrder():
    url = baseURI + order
    payload = {'id': 6, 'customerName': 'kiran'}
    headers = {"Content-Type": "application/json"}
    data, resp_status, timeTaken = postApidata(url, payload, headers)
    logger.info('Placing order without token')
    print(data)
    assert data.get("error") == 'Missing Authorization header.'
    assert resp_status == 401


def test009_PlaceOrder(get_token):
    token = get_token
    url = baseURI + order
    payload = {'id': '7', 'customerName': 'sagar'}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = postApidata(url, payload, headers)
    logger.info('Placing order with invalid user with token')
    print(data)
    assert "created" not in data
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
