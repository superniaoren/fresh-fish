
if __name__ == '__main__':
    print('=' * 40)
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

    # generator_expression = (expression for item in collection)
    # list comprehensions vs generator expressions
    print('=' * 40)
    genexpr = ('Saint' for i in range(3))
    listcomp = ['Boom' for i in range(3)] 
    print('Genexpr: ', genexpr)
    print('ListComp: ', listcomp)

    list_genexpr = list(genexpr)
    print('ListGenexpr: ', list_genexpr)

    # def generator(expression, collection):
    #   for item in collection:
    #       yield expression

    # filter value:
    # generator_expression = (expression for item in collection if condition)
    print('=' * 40)
    odd_squares = (x * x for x in range(10) if x % 2 == 1)
    for _ in range(5):
        print(next(odd_squares)) 

    # generator chains
    print('=' * 40)
    chains = (x * y for x in range(10) if x % 2 == 1
                for y in range(4) if y % 2 == 1)
    print(chains)
    for item in chains:
        print(item)
