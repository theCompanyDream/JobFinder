"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)"""

import yaml
import itertools
import locations

def parseFile(file=None):
    """
        Loads file and translates it into a generator function
    """
    fileLocation = file
    if fileLocation is None:
        fileLocation = locations.GetDefaultConfigFile()

    with open(fileLocation, 'r+') as stream:
        fileData = yaml.load(stream)
        fileData['Locations'] = [loc for loc in Dict_To_String_Generator(fileData['Locations'])]
        return fileData

def GetJobRequest(data):
    """
    Generator that gets the requirements for me
    """
    zippedParameters = list(itertools.product(data['Jobs'], data['Locations']))

    for x in zippedParameters:
        yield {'Search': x[0], 'Location': x[1]}

def BuildRequest(data, *defaultparams):
    """
        This Builds
    """
    WebsiteList = list(data['Websites'])
    JobRequest = GetJobRequest(data)
    while len(WebsiteList) > -1:
        try:
            searchdict = {key: data[key] for key in defaultparams}
            searchdict.update(next(JobRequest))
            searchdict['key'] = WebsiteList[0]['key']
            yield searchdict
        except StopIteration:
            JobRequest = GetJobRequest(data)
            WebsiteList.pop(0)



def Dict_To_String_Generator(diction):
    """
        Generator Function that concats a val, key
    """
    if diction:
        for key, val in [[v, k] for v, k in diction.items()]:
            for city in val:
                yield "{0},{1}".format(city, key)
    else:
        raise TypeError()

if __name__ == "__main__":
    data = parseFile()
    print(data)

    for x in GetJobRequest(data):
        print(x)

    print("ok this is new shit \n\n")

    for x in BuildRequest(data, "limit", 'radius'):
        print(x)
