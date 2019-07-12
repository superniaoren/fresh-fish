## Functions are the first-class in python

def yell(text):
    return text.upper() + ' ..'

def whisper(text):
    return text.lower() + ' ..'

def action(func):
    act = func('Where did you sprint out?')
    print(act)

if __name__ == '__main__':
    # basic 
    print(yell('you will come back'))

    # functions are objects
    yawl = yell
    print(yawl('winter is coming'))

    print('func.__name__:{}'.format(yell.__name__))
    print('func.__name__:{}'.format(yawl.__name__))
    del yell
    print('func.__name__:{}'.format(yawl.__name__))

    try:
        print('func.__name__:{}'.format(yell.__name__))
    except NameError:
        print('yell has been deleted')
    except:
        print('unexpected error ...')
        raise
        
    # functions can be stored in data structures
    funcs = [yawl, str.lower, str.capitalize]
    print(funcs)
    for f in funcs:
        print(f, f('bye, yo'))

    # functions can also be passed to other functions
    action(yawl)
    action(whisper)
    
