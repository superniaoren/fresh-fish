## 
## Python yield is confusing. It's always tied to Python genertor
## https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

if __name__ == '__main__':
    print('review and learn yield again: ')
    print('to understand what `yield` is, U should first understand what `generator` is. ') 
    # for example, create an iterable var:
    mylist = [x * x for x in range(5)]
    print('type of mylist: ', type(mylist))
    for i in mylist:
        print(i)
    # here  mylist is an iterable. everything you can use 'for ... in ...' on is an iterable.
    # these iterables are handy cause you can read them as much as you wish,
    # BUT you store all the values in memory and this is not always you want when you have 
    # a lot of values.

    # generators: Generators are iterables, a kind of iterable you can only iterate over once.
    print('Generators do NOT store all the values in memory, they generate the values on the fly.')
    mygenerator = (x * x for x in range(5))
    print('type of mygenerator: ', type(mygenerator))
    for i in mygenerator:
        print(i)


