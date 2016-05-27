"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)"""

import yaml, itertools


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
        locationList = [loc for loc in Dict_To_String_Generator(data['Locations'])]
        zippedParameters = itertools.product(data,data['Jobs'], locationList)
        for x in zippedParameters:
            print(x)
        



if __name__ == "__main__":
    location(r'C:\Users\company2\workspace\jobs\bin\request.yaml')
