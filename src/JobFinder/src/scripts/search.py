
def main(k, t,g, f, **kwargs):
    print("{0}, {1}, {2}, {3}".format(k,t,g,f))

dict = {'fs':324,'k': 1, 't': 2, 'g': 3, 'f': 4}

main(**dict)
