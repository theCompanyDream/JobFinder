
import os
from bravado.client import SwaggerClient

configDirectory = 'yaml'
swagPattern = '.swagger.yaml'

def GetDefaultConfigFile():
    """
        Returns the requests config file from dictionary
    """
    return "{0}{1}".format(os.path.dirname(__file__), r'\yaml\request.yaml')

def listSwaggerConfig():
    """
        Returns a list of only swagger configuration files
    """
    configDir = os.path.join(os.path.dirname(__file__), configDirectory)
    return { fileloc.replace(swagPattern, ''): os.path.join(configDir, fileloc)
        for fileloc in os.listdir(configDir) if swagPattern in fileloc}

class SwaggerApi(object):
    def __init__(self):
        self.data = listSwaggerConfig()

    def Get(self, key):
        """
            param: key for
        """
        loc = self.data[key]
        assert loc is not None
        print(loc)
        self.client = SwaggerClient.from_url("file:\\\\\\"+loc)
        return self.client

if __name__ == "__main__":
    print(GetDefaultConfigFile())
    print(listSwaggerConfig())
    swagger = SwaggerApi()
    print(swagger.Get("indeed"))
