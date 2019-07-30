
def dump_vector(x, y, z, w):
    print('<{0}, {1}, {2}, {3}>'.format(x, y, z, w))

if __name__ == '__main__':
    dict_args = {'cn': 13.6, 'us': 21.5, 'kr': 3.1, 'jp': 4.6}
    try:
        dump_vector(*dict_args)
    except:
        print("the args not match up!!!!")
    
    try:
        dump_vector(**dict_args)
    except:
        print("the args not match up!!!!")

    dict_match = {'x': 'enormous', 'y': 'stress', 'z': -0.5, 'w': 23}
    try:
        dump_vector(*dict_match)
    except:
        print("the args not match up!!!!")
    
    try:
        dump_vector(**dict_match)
    except:
        print("the args not match up!!!!")
