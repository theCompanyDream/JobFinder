
import os

configDirectory = 'yaml'
swagPattern = 'swagger.yaml'

def GetDefaultConfigFile():
    """
        Get the config file from dictionary
    """
    return "{0}{1}".format(os.path.dirname(__file__), r'\yaml\request.yaml')

def listSwaggerConfig():
    """

    """
    dir = "{0}\\{1}".format(os.path.dirname(__file__), configDirectory)
    return [fileloc for fileloc in  os.listdir(dir) if swagPattern in fileloc]

if __name__ == "__main__":
    print(GetDefaultConfigFile())
    print(listSwaggerConfig())
