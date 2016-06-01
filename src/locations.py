"""
Author: Timothy Brantley II

"""

import os
from bravado.client import SwaggerClient

configDirectory = 'yaml'
swagPattern = '.swagger.yaml'
schemaPattern = '.swagger.json'

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
        for fileloc in dirList if fileloc in swagPattern}

    dirDict.update()

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
    print(GetDefaultConfigFile())
    print(listSwaggerConfig())
    swagger = SwaggerApi()
