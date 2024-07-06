import requests, json


def GetApiData(url, headers):
    # headers = {'content-Type': 'application/json'}
    response = requests.get(url, verify=False)
    data = response.json()
    assert len(data) > 0, 'empty response'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def PostApidata(url, payload, headers):
    print('requesturl:', url)
    response = requests.post(url, json=payload, headers=headers)
    return response
