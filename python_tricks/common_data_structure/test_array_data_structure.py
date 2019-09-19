import array
# 1,[mutable/immutable]: item assignment, item deletion
# 2,hold arbitrary data types
if __name__ == '__main__':
    # standard array: the list are mutable, and can hold arbitrary data types
    print('-' * 20, " list, mutable dynmaic arrays ")
    arr = ['gold', 'pogoda', 'abudo']
    print(arr)
    del(arr[1])
    print(arr)
    arr.append(3.14115)
    print(arr)
    
    print('-' * 20, " tuple, immutable containers ")
    #tpl = ('bagger', 'vanish', 'puff')
    tpl = 'bagger', 'vanish', 'puff'
    print(tpl)
    #tpl[1] = 'release'  # immutable, not support item assignment
    #del(tpl[1])   # neither support item deletion
    # tuple concatenation !!!  (1) is type of int, not tuple
    tpl = tpl + (33.0,)  #  can only concatenate tuple (not "float") to tuple
    tpl = tpl + (33,)  # so, must use (int/float,), not (int/float)
    print(tpl)

    print('-' * 20, " array, basic typed arrays")
    tarr = array.array('f', [-9.0, 8.0, -7.0, 6.0])
    print('nice repr: ', tarr)
    tarr[3] = -5.0  
    print('mutable: ', tarr)
    del(tarr[1])
    print('mutable: ', tarr)
    tarr.append(4.0)
    print('mutable: ', tarr)
    #tarr[3] = 'typed' # so must be the 'type', here should be float
    
    print('-' * 20, " str, immutable arrays of unicode charactors")
    sarr = 'remind us people of night'
    #sarr[1] = 'A'  # immutable, 
    #del(sarr[3])   # immutable
    larr = list(sarr)
    print('can be unpacked into a list, to get a mutable repr: ')
    print(larr)
    marr = ''.join(list(sarr))
    print('back to immutable string: ', marr)
    #del(marr[0])
    print("strings are recursivee data structures: ", type(sarr), type(sarr[0]))

    # unsigned char, [0, 255]
    print('-' * 20, " bytes, immutable arrays of single bytes")
    barr = bytes((255, 254))
    print('immutable: ', barr)
    #barr[0]
    #del(barr[1])

    print('-' * 20, " bytearray, dedicated mutable arrays of single bytes")
    darr = bytearray((2, 24, 241))
    print('bad repr: ', darr)
    darr[1] = 255
    print('mutable: ', darr)
    del(darr[2])
    print('mutable: ', darr)
    darr.append(23)
    print('mutable: ', darr)
    #darr[2] = 'should-not-str'  # integer is required
    #darr[2] = 256  # range (0, 256)
    carr = bytes(darr)
    print('can be converted back to into bytes:')
    print(carr)
    bdarr = bytearray(carr)
    print('can be converted back to into bytearray:')
    print(bdarr)


