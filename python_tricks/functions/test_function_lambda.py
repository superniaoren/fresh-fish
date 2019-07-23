## lambdas are single-expression functions
## providing a shortcut for declaring small anonymous functons
import operator


if __name__ == '__main__':
    # simplest examples
    add = lambda x, y: x + y
    print(add(5, 3))
    mul_var = (lambda x, y: x * y)(5, 3)
    print(mul_var)

    # key functions in sort 
    org = [(1, 'pan'), (2, 'pants'), (3, 'turtle'), (4, 'new_boy')]
    new = sorted(org)
    print(new)
    #new = sorted(org, key=lambda x: x[1])
    new = sorted(org, key=operator.itemgetter(1))
    print(new)

    #new2 = sorted(range(-4, 4), key=lambda x: x * x, reverse=True)
    new2 = sorted(range(-4, 4), key=abs, reverse=True)
    print(new2)
    
    # lexical closures
    def make_mod(n):
        return lambda x: x % n
        #return lambda x: if n != 0: x % n

    mod_3 = make_mod(3)
    mod_0 = make_mod(0)
    
    var_3 = mod_3(10)
    #var_0 = mod_0(51)
    print(var_3)
    
