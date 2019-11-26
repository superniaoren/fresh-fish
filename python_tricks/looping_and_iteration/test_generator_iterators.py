

def InfiniteRepeater(value):
    while True:
        yield value

def TwoTimesRepeater(value):
    yield(value)
    yield(value)

def FiniteRepeater(value, counter):
    if counter <= 0:
        counter = 5

    current = 0
    while True:
        if current < counter:
            current += 1
            #yield value
            yield current
        else:
            return

def BoundedRepeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

if __name__ == '__main__':
    print('generater based iterator: ')
    
    for x in InfiniteRepeater('Infinite'):
        print(x)
        break  # for test, exit infinite loop

    max_repeats = 10
    for x in FiniteRepeater('Finite', max_repeats):
        print(x)
    
    for x in BoundedRepeater('Bounded', max_repeats):
        print(x)
    
    for x in TwoTimesRepeater('Two'):
        print(x)
    
    twoIter = TwoTimesRepeater('two')
    print(next(twoIter))
    print(next(twoIter))
    print(next(twoIter))
