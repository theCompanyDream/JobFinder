import requests

def callIndeed(parameters):
    request = requests.get('http://api.indeed.com/ads/apisearch', params = parameters)
    return request
