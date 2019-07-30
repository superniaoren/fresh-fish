
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
    print(pretend(0))
    print(pretend_none(0))
    print(pretend_default(0))
    
