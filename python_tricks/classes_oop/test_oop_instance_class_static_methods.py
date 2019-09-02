# 1, 'instance method need a class instance and can access the instance through self'
# 2, class methods can't access the instance(self) but they have access to the class 
#    itself via cls.
# 3, 

class EFClass:
    # is a regular instance method. through self parameter, instance methods can freely
    # access attributes and other methods on the same object.
    # instance methods can also access the class itself through the self.__class__ attribute.
    # instance methods are powerful in terms of access restrictions-they can freely modify state
    # on the object instance and on the class itself.
    def instancemethod(self):
        return 'instance method ', self
    
    # since the class method only has access to this cls argument, it can't modify object instance 
    # state.That would require access to self.  
    @classmethod
    def classmethod(cls):
        return 'class method ', cls

    # this type of method doesn't take a self or a cls parameter, although, it can be made to accept 
    # an arbitrary number of other parameters.
    # confirm that static methods can neither access the object instance state nor the class state.
    @staticmethod
    def staticmethod():
        return 'static method '

class Pizza:
    def __init__(self, foods):
        self.foods = foods
    def __repr__(self):
        return f'Pizza ({self.foods!r})'

    @classmethod
    def pizza_1(cls):
        return cls(['yang', 'niu'])

    @classmethod
    def pizza_2(cls):
        return cls(['luke', 'nound', 'shawn'])

if __name__ == '__main__':
    efc = EFClass()
    # instance method
    print("efc self: ", efc.instancemethod()) 
    #print("efc obj: ", efc.instancemethod(efc))  # error
    print("EFC obj: ", EFClass.instancemethod(efc))
    print("efc obj->class: ", efc.__class__.classmethod())

    # class method
    print("efc class: ", efc.classmethod())
    print("efc class: ", EFClass.classmethod())

    # static method
    print('efc static: ', efc.staticmethod())
    print('efc static: ', EFClass.staticmethod())
    #print('efc static: ', EFClass.staticmethod(efc))

    # static method: 
    # can't access class or instance state because they don't take a 'cls' or 'self' argument.
    # flagging a method as a static method is not just a hint that a method won't modify class 
    #    or instance state. This restriction is also enforced by the Python runtime.
    # In practice, it often helps avoid accidental modification that go against the original design.

    # static & class methods are ways to communicate developer intent while enforcing that intent
    #    enough to avoid most 'slip of the mind' mistakes and bugs that would break the design

    # class: factory methods ? 
    # Here defind alternative constructors for your classes
    # Python only allows one __init__ method per class. Using class methods makes it possible to add
    # as many alternative constructors as neccessary.
    print(Pizza.pizza_1())
    print(Pizza.pizza_2())



