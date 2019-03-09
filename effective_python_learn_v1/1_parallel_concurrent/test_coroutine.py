##
import os, sys

def my_coroutine():
    while True:
        recieve = yield
        print('received: ', recieve)

def minimize_coroute():
    # taken as the 1st input & minimize value
    minimize = yield
    while True:
        input_value = yield minimize
        minimize = min(input_value, minimize)
    # although U wanna return a value, the type is still 'generator'
    #return minimize

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
    # Generators are iterators, a kind of iterable you can only iterate over once. 
    # Generators do not store all the values in memory, they generate the values on the fly:
    
    it = my_coroutine()
    print('type: ', type(it))
    next(it)
    it.send('1st')
    it.send('2nd')

    mini_it = minimize_coroute()
    print('type: ', type(mini_it))
    next(mini_it)
    print(mini_it.send(10))
    print(mini_it.send(30))
    print(mini_it.send(5))
    print(mini_it.send(1))
