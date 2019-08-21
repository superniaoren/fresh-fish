# named tuple, create immutable class
from collections import namedtuple

if __name__ == "__main__":
    # 1, ordinary built-in tuple
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

    # 2, now, the class  is Rain, but named by HeavyRain,U can't use Rain directly
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

    # 3, unpack tuple
    cloud, wind, temp = today_Beijing
    print("[nnpack tuple]: cloud={0}, wind={1}, temp={2} ".format(cloud, wind, temp))    
    print("[operator *]: ", *breakfast)

    # 4, subclassing namedtuples
    BeesKnees = namedtuple("Whatevername", "Vast Chosen")
    class Huangdouduo(BeesKnees):
        def theExcellent(self):
            self.Bees =  self.Vast * -1
            if self.Chosen:
                self.Bees += 10
                return self.Vast + 1000
            else:
                return self.Vast - 1000

    bk = Huangdouduo(314, True)
    print(bk.theExcellent)
    print(bk.theExcellent())

    # 5, namedtuples' __fields property; you can use 'Class' name or object
    print("Huangdouduo's fields: ", bk._fields)
    print("Huangdouduo's fields: ", BeesKnees._fields)
    print("Food's fields: ", Food._fields)

    CNFood = namedtuple("Whatevername", Food._fields + ('dumplin', 'burgers'))
    print("CNFood's fields: ", CNFood._fields)
    
