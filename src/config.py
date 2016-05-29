"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)"""

import yaml, itertools

def parseFile(file):
    """
        Loads file and translates it into a generator function
    """
    with open(file, 'r+') as stream:
        data = yaml.load(stream)
        data['Locations'] = [loc for loc in Dict_To_String_Generator(data['Locations'])]
        return data


def GetJobRequest(data):
    "formats the job part of the document"
    zippedParameters = list(itertools.product(data['Jobs'], data['Locations']))

    for x in zippedParameters:
        yield {'Search': x[0], 'Location': x[1]}


def BuildRequest(data, *defaultparams):
    WebsiteList = list(data['Websites'])
    JobRequest = GetJobRequest(data)

    while len(WebsiteList) > 0:

        try:
            searchdict = {key:data[key]  for key in defaultparams}
            searchdict.update(next(JobRequest))
            searchdict['key'] = WebsiteList[0]['key']
            yield searchdict
        except StopIteration:
            JobRequest = GetJobRequest(data)
            WebsiteList.pop()



def ConvertRentalRequest(payload):
    "transforms and prepares it for rentals requests"
    pass

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
    data = parseFile(r'C:\Users\company2\workspace\JobFinder\bin\request.yaml')
    print(data)
    
    for x in GetJobRequest(data):
        print(x)

    print ("ok this is new shit \n\n")

    for x in BuildRequest(data, "results", 'radius'):
        print(x)
