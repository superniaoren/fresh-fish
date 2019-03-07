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

    # generators: NOTE the difference between tuple and generator !!
    # a = ('cc', 23) --> tuple;  b = (x * x for x in range(10)) -> generator
    
