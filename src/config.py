"""
Author: Timothy Brantley II
This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)
"""

import yaml
import itertools
from locations import GetDefaultConfigFile

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



if __name__ == "__main__":
    data = parseFile()
    print(data)

    for x in GetJobRequest(**data):
        print(x)

    print("ok this is new shit \n\n")

    for x in BuildRequest("limit", 'radius', **data):
        print(x)
