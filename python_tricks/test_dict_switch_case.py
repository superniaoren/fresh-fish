import operator

# basic imple. of switch-case function
def dispatch_if(op_name, arg_a, arg_b):
    if op_name == 'add':
        return arg_a + arg_b
    elif op_name == 'sub':
        return arg_a - arg_b
    elif op_name == 'mul':
        return arg_a * arg_b
    elif op_name == 'div':
        return arg_a / arg_b
    else:
        raise ValueError('not support operation {}'.format(op_name))

def dispatch_dict(op_name, arg_a, arg_b):
    return {
        'add': lambda: arg_a + arg_b,
        'sub': lambda: arg_a - arg_b,
        'mul': lambda: arg_a * arg_b,
        'div': lambda: arg_a / arg_b,
    }.get(op_name, lambda: None)()
    # error:
    #}.get(op_name, lambda: None)(arg_a, arg_b)
    #}.get(op_name, lambda: None)

if __name__ == '__main__':
    a = 100
    b = 32
    
    op_name = 'exp'
    print('op:{0}, a-op-b={1}'.format(op_name, dispatch_dict(op_name, a, b)))

    op_name = 'mul'
    print('op:{0}, a-op-b={1}'.format(op_name, dispatch_dict(op_name, a, b)))

    op_name = 'div'
    print('op:{0}, a-op-b={1}'.format(op_name, dispatch_if(op_name, a, b)))
