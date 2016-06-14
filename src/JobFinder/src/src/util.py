

def Dict_To_String_Generator(diction):
    """
        Generator Function that concats a val, key
        TODO: better name and make format lambda
    """
    if diction:
        for key,val in [[v, k] for v, k in diction.items()]:
            for city in val:
                yield "{0}, {1}".format(city, key)
    else:
        raise TypeError()
