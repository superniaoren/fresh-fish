import functools
# args and kwargs are optional, args can be viewed as a tuple
# and kwargs could be a dict.
def scott_foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

def mutable_foo(required, *args, **kwargs):
    kwargs['actor'] = 'YueYunP'
    new_args = args + (1001, )
    scott_foo(required, *new_args, **kwargs)

def trace(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        print(f, args, kwargs)
        ret = f(*args, **kwargs)
        print(ret)
    return decorated_func

@trace
def greet(greeting, name):
    return '{}, {} !!'.format(greeting, name)

if __name__ == '__main__':
    print("use *args and **kwargs to accept optional arguments")
    scott_foo("day and night")
    print('-' * 40)
    scott_foo("nignt and day", 31514, 45678)
    print('-' * 40)
    scott_foo("NIGNT AND DAY", 3.14159, -45678, key1='telescope', key2=990)
    print('-' * 40)
    mutable_foo("NIGNt and dAY", 0.10059, -78, key1='iCar', key2=-90)
    print('-' * 40)

    greet('Night', "Zooo")
