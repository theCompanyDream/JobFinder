"""
Author: Timothy Brantley II
This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)
"""

import yaml
import itertools
import os
from bravado.client import SwaggerClient

configDirectory = 'yaml'
swagPattern = '.swagger.yaml'
schemaPattern = '.swagger.json'

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

def parseFile(file=None):
    """
        Loads file and translates and returns a generator function

        :param file The location of the file
        :returns dictionary of yaml configuration
    """
    fileLocation = file
    if fileLocation is None:
        fileLocation = GetDefaultConfigFile()

    with open(fileLocation, 'r+') as stream:
        fileData = yaml.load(stream)
        fileData['Locations'] = [loc for loc in Dict_To_String_Generator(fileData['Locations'])]
        return fileData

def GetJobRequest(**kwargs):
    """ Generator that gets the requirements for me
        :param data dictionary that gets the combination of 'Jobs'
        :param ty
        :returns dictionary
    """
    zippedParameters = list(itertools.product(kwargs['Jobs'], kwargs['Locations']))

    for x in zippedParameters:
        yield {'Search': x[0], 'Location': x[1]}

def BuildRequest(*defaultparams, **kwargs):
    """ This Generator maps the large responses of data

        :param defaultparams dictionary values to be returned
        :type string
        :param kwargs dictonary that is going to be returned
        :type dictionary
        :rtype dictionary

    """
    WebsiteList = list(data['Websites'])
    JobRequest = GetJobRequest(**kwargs)
    while len(WebsiteList) > -1:
        try:
            searchdict = {key: data[key] for key in defaultparams}
            searchdict.update(next(JobRequest))
            searchdict['key'] = WebsiteList[0]['key']
            yield searchdict
        except StopIteration:
            JobRequest = GetJobRequest(**kwargs)
            WebsiteList.pop(0)



def Dict_To_String_Generator(diction):
    """
        Generator Function that concats a val, key
    """
    if diction:
        for key,val in [[v, k] for v, k in diction.items()]:
            for city in val:
                yield "{0},{1}".format(city, key)
    else:
        raise TypeError()

class DataParameters():
    def __init__(self, file):
        self.data = parseFile(file)

def MapValues(mappingDictionary, requestDictionary):
    return {key: requestDictionary.get(val, '') for key, val in mappingDictionary.items()}

def GetDefaultConfigFile():
    """ Returns the requests config file from dictionary
        :rtype str or unicode
        :return str or unicode
    """
    return "{0}{1}".format(os.path.dirname(__file__), r'\yaml\request.yaml')

def listSwaggerConfig():
    """
        Returns a list of only swagger configuration files
    """
    configDir = os.path.join(os.path.dirname(__file__), configDirectory)
    dirList = os.listdir(configDir)

    dirDict = {fileloc.replace(swagPattern, '') :os.path.join(configDir, fileloc)
        for fileloc in dirList if swagPattern in fileloc}

    dirDict.update({'schema': os.path.join(configDir, 'schema.v2.modified.swagger')})

    return dirDict



class SwaggerApi(object):
    """

    """
    def __init__(self):
        self.data = listSwaggerConfig()

    def Get(self, key):
        """
            param: key for
        """
        loc = self.data[key]
        assert loc is not None
        return SwaggerClient.from_url("file:\\\\\\"+loc)

if __name__ == "__main__":
    data = parseFile()
    print(data)
    # print(GetDefaultConfigFile())
    # print(listSwaggerConfig())
    #
    # for x in GetJobRequest(**data):
    #     print(x)
    #
    # print("ok this is new shit \n\n")
    swagger = SwaggerApi()
    client = swagger.Get('indeed')
    dict = MapValues(IndeedDict, data)
    valList = [val for key, val in IndeedDict.items()]
    print("hello\n", dict,"\nVal List", valList)

    for x in BuildRequest(*valList, **data):
        print(x)


    print(client)

    print(indeedDict)
    # print("This is the new Mappings\n{0}".format(indeeddict))
