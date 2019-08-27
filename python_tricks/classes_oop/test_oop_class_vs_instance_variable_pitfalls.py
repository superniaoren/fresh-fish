# python's object model distinguishes between class and instances variables.


# class variables: they are not tied to any particular instance of a class. 
# instead, class variabls store their contents on the class itself, and all objects 
# created from a particular class share access to the  same set of class variables.

class JiGong:
    hobbies = 'buddha'
    counter= 0

    def __init__(self, name):
        self.who = name
        self.__class__.counter += 1

class Counter:
    num_counter = 0
    
    def __init__(self, value):
        self.num_counter += 20
        #self.__class__.num_counter += value

class BuggyCounter:
    num_counter = 0 
    def __init__(self):
        self.num_counter += 1

if __name__ == '__main__':
    # init
    luck = JiGong('xiuyuan')
    taiz = JiGong('daoji')

    print('who: ', luck.who, taiz.who)
    print('hobbies: ', luck.hobbies, taiz.hobbies)

    # modify the class variable
    # here create an instance variable with the same name as the class variable
    # NOTE: this is error-prone and is the key difference, do care about it. 
    luck.hobbies = 'pogada'
    taiz.hobbies = 'talkie'
    print('hobbies: ', luck.hobbies, taiz.hobbies)

    # Reason: 'trying to modify a class variable through an object instance-which then 
    #         accidently creates an instance variable of the same name, shadowing the 
    #         original class variable-is a bit of an OOP pitfall in Python'
    # fetch the class var
    print('type of inst var: ', type(luck.hobbies))
    print('type of inst var: ', type(taiz.hobbies))
    print('class hobbies: ', luck.__class__.hobbies, taiz.__class__.hobbies)
    
    # class var 
    print('another class: ', JiGong.hobbies)

    # class counter var
    print('JiGong class: ')
    print(JiGong('').counter)
    print(JiGong('').counter)
    print(JiGong.counter)
    print(JiGong('').counter)
    print(JiGong('').counter)

    # bug 1
    print('buggy counter 1: ')
    print(Counter(0).num_counter)  # self.num_counter, an copy
    print(Counter.num_counter)  # class.num_counter
    print(Counter.num_counter)
    counter_1 = Counter(1)
    print(counter_1.num_counter, counter_1.__class__.num_counter)
    counter_2 = Counter(1)
    print(counter_2.num_counter, counter_2.__class__.num_counter)
    counter_3 = Counter(1)
    print(counter_3.num_counter, counter_3.__class__.num_counter)
    counter_4 = Counter(1)
    print(counter_4.num_counter, counter_4.__class__.num_counter)

    # bug 2, BuggyCounter() is an instance, while BuggyCounter is just the class
    # hencefore you can find the counter of class stay unchanged. 
    print('buggy counte 2: ')
    print(BuggyCounter.num_counter)
    print(BuggyCounter().num_counter)# here return the instance 'num_counter'
    print(BuggyCounter.num_counter)  # class num_counter not increased
    print(BuggyCounter().num_counter)
    print(BuggyCounter.num_counter)
    print(BuggyCounter().num_counter)

    # where's the bug from: class variables can be 'shadowed' by instance
    # variable of the same name. it;s easy to (accidently) override 
    # class variable in a way that introduces bugs and odd behavior.

