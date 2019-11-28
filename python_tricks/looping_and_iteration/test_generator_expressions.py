
if __name__ == '__main__':
    print('test generator expressions: ')
    iterator = (i for i in range(4))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    #print(next(iterator))  # StopIteration
