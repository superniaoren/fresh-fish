
if __name__ == '__main__':
    print('test generator expressions: ')
    iterator = (i for i in range(4))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    #print(next(iterator))  # StopIteration

    def bounded_repeater(value, max_counter):
        for i in range(max_counter):
            yield value

    iterator = bounded_repeater('Sadiago', 4)
    #print(next(iterator))
    #print(next(iterator))
    #print(next(iterator))
    #print(next(iterator))
    for x in iterator:
        print(x)

    #next(iterator)

    # list comprehensions vs generator expressions
    genexpr = ('Saint' for i in range(3))
    listcomp = ['Boom' for i in range(3)] 
    print('Genexpr: ', genexpr)
    print('ListComp: ', listcomp)
