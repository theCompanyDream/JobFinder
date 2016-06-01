"""
    Author: Timothy Brantley Ii
    This file maps the yaml files to the web files
    I use dictionaries here becuase it doesn't seem like the
"""

IndeedDict = {
    'Publisher': 'key',
    'format' : 'format',
    'v': 'v',
    'q': 'Jobs',
    'l': 'Locations',
    'radius': 'radius',
    'jt' : 'JobTypes',
    'limit' : 'limit',
    'fromage' : 'TimeSpan',
    'latlong' :  'ShowGeo',
    'useragent': 'userAgent'
}    

def MapValues(mappingDictionary, requestDictionary):
    return {requestDictionary[val] for key, val in mappingDictionary.items()}

if __name__ == "__main__":
    payload = {'limit': 200, 'key': 3, 'Location': 'Oakland,California', 'Search': 'Devops', 'radius': 30}
    p = MapValues(IndeedDict, payload)
    print(p)
