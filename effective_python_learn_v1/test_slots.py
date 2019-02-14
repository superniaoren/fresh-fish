##
##
import os, sys
import timeit
from timeit import Timer

class withoutSlots:
    #__dict__ = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        

class withSlots:
    __slots__ = ('x', 'y', 'z')
    #__dict__ = ('x', 'y', 'z')
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
def instance_fn(cls):
    def instance():
        x = cls(1, 2, 3)
    return instance

def get_set_fn(cls):
    print(list(range(26)))
    # [zoo] TODO: error fix !!
    x = cls(list(range(26)))
    def get_set():
        ...
        #x.y = x.z - 1
        #x.a = x.b - 1
        #x.d = x.q - 2
        #x.i = x.j + 1
    return get_set


# ref:  https://docs.python.org/3/library/timeit.html
# Seems: when use __slots__ or __dict__ in withSlots class, U can see the speedup
# but when U use __dict__ in withoutSlots, it has bigger latency.
# the results need to be re-evaluated !!!

if __name__ == '__main__':
    print("test slots with/without")
    number = 50000
    x = 1
    y = 10
    z = 100
    var_withslots = withSlots(x, y, z)
    var_withoutslots = withoutSlots(x, y, z)
    T = Timer()

    try:
        #with_time = timeit.timeit(instance_fn(withSlots), number=number)
        with_time = T.timeit(get_set_fn(withSlots), number=number)
        print('withSlots time = {}'.format(with_time))
    except:
        T.print_exc()
    
    try:
        #without_time = timeit.timeit(instance_fn(withoutSlots), number=number)
        without_time = T.timeit(get_set_fn(withoutSlots), number=number)
        print('withoutSlots time = {}'.format(without_time))
    except:
        T.print_exc()

