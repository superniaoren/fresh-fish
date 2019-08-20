
from collections import namedtuple

if __name__ == "__main__":
    # ordinary built-in tuple
    tup = ('guodegang', object(), 51)
    print(tup)
    try:
        tup[2] = -51
    except TypeError:
        print('tuple type is immutable, should not assignment')
    print('-' * 40)

    ## downside of plain tuples: the data you sotre in them can only
    ## be pulled out by accessing it through integer indices. 
    ## this can impact code readability

    # now, the class  is Rain, but named by HeavyRain,U can't use Rain directly
    HeavyRain = namedtuple('Rain', 'cloud wind temperature')
    print(type(HeavyRain))
    #print(type(Rain))
    print(HeavyRain)

    today_Beijing = HeavyRain('B', 4, 21)
    #NOTE: today_Beijing = Rain('B', 4, 21)  # error
    print(today_Beijing)
    print('-' * 40)

    # food, hungrary now ...
    Food = namedtuple('Food', [
                                'toast',
                                'eggybread',
                                'bagel',
                                'muffim',
                                'pancake',
                     ])
    breakfast = Food(True, False, False, False, True)
    print(breakfast)
    # you can still access the values by their index
    print(breakfast.toast, breakfast[4])  # error: ['toast']
    print('-' * 40)
