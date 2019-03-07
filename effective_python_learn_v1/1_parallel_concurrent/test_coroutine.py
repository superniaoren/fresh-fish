##
import os, sys


if __name__ == '__main__':
    # iterators: store all the values in memory; not memory-efficient
    #list_a = [1, 2, 3, 6]
    #for i in list_a:
    #    print(i)
    
    list_b = [x * x for x in range(3)]
    for i in list_b:
        print(i)

    # generators:
    
