# programmers should know the ins and outs of the language they're working with
# after all, code is communication
# today's topic: implicit return statement
def pretend(value):
    if value:
        return value
    else:
        return None

def pretend_none(value):
    """ bare return, implies `return None` """
    if value:
        return value
    else:
        return 

def pretend_default(value):
    """ missing return statement, implies `return None` """
    if value:
        return value
    #return 

if __name__ == '__main__':
    print(type(pretend(0)))
    print(type(pretend_none(0)))
    print(type(pretend_default(0)))
    print('-' * 40)
    print(pretend(0))
    print(pretend_none(0))
    print(pretend_default(0))
    
