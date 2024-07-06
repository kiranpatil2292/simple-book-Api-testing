import requests,json


def getApiData(url, headers):
    # headers = {'content-Type': 'application/json'}
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    json_data = json.dumps(data, indent=4)
    print(json_data)
    assert len(data) > 0, 'empty response'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def postApidata(url, payload, headers):
    # headers = {'content_Type': 'application/json'}
    print('requesturl:', url)
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def putdata(url, body,headers):
    # headers = {'content_Type': 'application/json'}
    print('requesturl:', url)
    response = requests.put(url, json=body, headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def deletedata(url, opheader=None):
    headers = {'content-Type': 'application/json'}
    headers = (headers | opheader) if isinstance(opheader, dict) else headers
    response = requests.delete(url, verify=False, headers=headers)
    print(response, requests, headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken
