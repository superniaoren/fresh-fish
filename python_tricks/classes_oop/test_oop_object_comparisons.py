# '==' vs 'is'
# the difference in meaning between 'equal' and 'identical'.
# 'is' operator: checking for identity, two vars point to the same object
# '==' operator: checking for equality, same type, same content, different objects
# 

if __name__ == '__main__':
    a = [9, 8, 7]
    b = a
    c = list(a)
    print('[equality] a == b: ', a == b)
    print('[identity] a is b: ', a is b)
    print('[equality] a == c: ', a == c)
    print('[identity] a is c: ', a is c)
    
