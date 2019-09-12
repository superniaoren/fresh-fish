
# basic common data structure

if __name__ == '__main__':
    # plane dict
    print('test basic dict: ')
    postIds = {
        'tiger': 9527,
        'wusong': 7295,
        'lice': 3719,
    }
    print('postIds: ', postIds)

    squares = [x * x for x in range(6)]
    print('squares list: ', squares)

    square = {x * x for x in range(6)}
    print('squares dict: ', square)

    # python's dictionaries are indexed by keys that can be of any
    # hashable type: A hashable object has a hash value which never 
    # changes during its lifetime (__hash__), and it can/should be 
    # compared to other object (__eq__). In addition, hashable objects
    # which compare as equal must have the same value.

    print(squares.__hash__)
    print(square.__hash__)

    # mutable type vars can NOT be used as dictionary keys.
    # immutable types like strings and numbers are hashable and work well
    # as dictionary keys. 'tuple' objects can also be used as dictionary
    # keys as long as as they contain ONLY hashable types themselves.

    print('test ordered dict: ')
    from collections import OrderedDict
    
    od = OrderedDict(two=1, one=3, three=4)
    print("ordered od: ", od)
    #print("ordered dict val: ", od['zoo'])
    print("ordered od.keys: ", od.keys())
    
    from collections import defaultdict
    dd = defaultdict(list)
    print("default dict: ", dd)
    print("default dict val: ", dd['zoo'])


