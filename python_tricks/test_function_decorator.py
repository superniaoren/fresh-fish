## decorators allow you to extend and modify the behavior of 
## a callable (functions, methods, and classes) WITHOUT 
## permanently modifying the callable itself.

# wrap some function
def dump_decorator(func):
    print('dump wrap:')
    return func

def uppercase(func):
    def wrapper(input):
        org_val = func(input)
        mod_val = org_val.upper()
        return mod_val
    return wrapper

def Asimovf(func):
    def wrapper():
        return '<head>' + func() + '</head>'
    return wrapper

def bolder(func):
    def wrapper():
        return '<bold>' + func() + '</bold>'
    return wrapper

#@dump_decorator
def salute(input_str):
    return input_str

@uppercase
def greet(input_str):
    return input_str

@Asimovf
@bolder
def hello():
    return 'Heloha'

if __name__ == '__main__':
    print('Decorators::')
    print('\t understanding decorator is a milestone for any Python programmer.')

    # basic 
    print(salute)
    salute = dump_decorator(salute)
    print(salute('bitcoin invented by Zuck?'))
    
    # mofify the behavior
    print(greet('Libra invented by Zuck!'))

    print(dump_decorator)
    print(salute)
    print(uppercase(greet))
    print(greet)
    
    # apply multiple decorators, like stacking mutli-functions
    print(hello())

    # decorate functions that acccept arguments
    




