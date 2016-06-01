import requests
import RequestBuilder

def call(url, **parameters):
    yield from requests.get(url, params = parameters)



# def buildRequets(Websites, **kwargs):
#     switcher = {
#         'Indeed': Indeed
#     }
#
#     for x in kwargs.items():
#         requestObj =  switcher.get(key['name'], lambda: "nothing")
#         yield requestObj(Websites, kwargs)
#
#     raise StopIteration

if __name__ == "__main__" :
    preparedRequests = RequestBuilder.parseFile()
