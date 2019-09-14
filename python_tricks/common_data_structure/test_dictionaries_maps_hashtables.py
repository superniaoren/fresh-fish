
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
    # accessing a missing 'key' creates it and initializes it using 
    # the default factory, 
    dd['meng'].append('R')
    dd['meng'].append('U')
    dd['meng'].append('S')
    dd['meng'].append('T')
    print('dd[\'meng\']: ', dd['meng'])

    # the data structure groups multiple dictionaries into a single mapping.
    # lookups search the underlying mappings one by one until a key is found.
    # insertions, updates, and deletions only affect the first mapping added to the chain.
    from collections import ChainMap
    dict1 = {'one': 1, 'two': 2}
    dict2 = {'two': 3, 'three': 3}
    dict3 = {'two': 2, 'four': 4}
    chain = ChainMap(dict1, dict2, dict3)
    print('ChainMap: ', chain)
    print('chain[\'two\'] = ', chain['two'])
    del(chain['two'])
    print('dict1: ', dict1)
    print('dict2: ', dict2)
    print('dict3: ', dict3)
    print('chain[\'two\'] = ', chain['two'])
    #print('chain[\'missing\'] = ', chain['missing'])

    # It is a wrapper around a standard dictionary that provides a read-only view 
    # into the wrapper dictionary's data.
    from types import MappingProxyType
    writable = {'one': 1, 'two': 2}
    read_only = MappingProxyType(writable)
    print('read_only: one = ', read_only['one'])
    read_only['one'] = 3.18
    writable['one'] = 3.19
    print('read_only: one = ', read_only['one'])
    print('mappingproxy: read_only: ', read_only)
