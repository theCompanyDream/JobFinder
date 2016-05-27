"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)"""

import yaml


def Dict_To_String_Generator(diction):
    """
        Generator Function that concats a val, key
    """
    if diction:
        for key, val in [[v,k] for v,k in diction.items()]:
            for city in val:
                yield "{0},{1}".format(city, key)
    else:
        raise TypeError()

def location(file):
    """
        Loads file and translates it into a generator function
    """
    with open(file, 'r+') as stream:
        data = yaml.load(stream)

        for x in Dict_To_String_Generator(data['Locations']):
            print(x)

        for loc,key in data['Websites'].items():
            data['token'] = key['key']
            data['url'] = key['url']
            print(loc)
            print(key)

        #print(data)

class Request(object):
    def __init__(self, file):
        with open(file, 'r+') as stream:
            self.data = yaml.load(stream)

if __name__ == "__main__":
    location(r'C:\Users\company2\workspace\jobs\bin\request.yaml')
