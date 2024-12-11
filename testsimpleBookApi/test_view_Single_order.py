import logging
from utils.myconfigparser import getPetApiURL

logger = logging.getLogger(__name__)
from utils.myutils import getApiData, postApidata

baseURI = getPetApiURL()


#view single order
def test0010_View_SingleOrder(place_order, get_token):
    token = get_token
    orderid = place_order
    print(orderid)
    # url = baseURI + path.format(orderid=orderid)
    url = baseURI + f'/orders/{orderid}'
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = getApiData(url, headers)
    print(data)
    logger.info('user can able to view single order')
    assert resp_status == 200
    assert data.get("orderId") == orderid


# view order with invalid order ID
def test0011_View_SingleOrder_invalid(get_token, place_order):
    token = get_token
    orderid = "invalid_order_id"
    url = baseURI + f'/orders/{orderid}'
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = getApiData(url, headers)
    print(data)
    logger.info('user cannot view order of invalid orderId')
    assert resp_status == 404  # Assuming 404 Not Found for invalid order ID
    assert data.get("error") == 'Order not found'


# view the order with invalid token
def test0011_View_SingleOrder_with_invalidToken(get_token, place_order):
    token = "bvfbvjn923i92nsmdsmdqwqieiwebvjvffjgidfdkkfdkf"
    orderid = place_order
    url = baseURI + f'/orders/{orderid}'
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data, resp_status, timeTaken = getApiData(url, headers)
    print(data)
    logger.info('user cannot view order of invalid token')
    assert resp_status == 401 , "Assuming Anuthorized for invalid token"
    assert timeTaken <4

