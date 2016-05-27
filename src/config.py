"""This script prompts a user to enter a message to encode or decode
using a classic Caeser shift substitution (3 letter shift)"""

import yaml


#Locations = lambda x : lambda  y : "{0},{1}".format(x, y)


def location(file):
    """
        Loads file and translates it into a generator function
    """
    with open(file, 'r+') as stream:
        data = yaml.load(stream)
        print(data)


if __name__ == "__main__":
    location(r'C:\Users\company2\workspace\jobs\bin\request.yaml')
