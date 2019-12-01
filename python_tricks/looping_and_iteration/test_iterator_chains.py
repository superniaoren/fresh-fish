# by ciaining together multiple iterators U can write highly efficient 
# data processing pipelines.

# blow-mind.
def integer(size):
    for i in range(size):
        yield i

def square(input):
    #yield x * x
    for x in input:
        yield x * x

def negated(input):
    #yield -x  # bad operator
    for x in input:
        yield -x

# follow the behavior of generators: data processing happens one element at a time.
# No buffering between the processing steps in the chain.
if __name__ == '__main__':
    print('test iterator chains ')

    size = 10
    list_val = list(negated(square(integer(size))))
    print(list_val)

    integers = range(10)
    squared = (x * x for x in integers)
    negates = (-x for x in squared)
    print(list(negates))
