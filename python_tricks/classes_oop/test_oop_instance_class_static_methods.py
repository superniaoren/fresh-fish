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
    @staticmethod
    def staticmethod():
        return 'static method '

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

    #
