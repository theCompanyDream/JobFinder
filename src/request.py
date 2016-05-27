import requests

def callIndeed(url, parameters):
    request = requests.get(url, params = parameters)
    return request
