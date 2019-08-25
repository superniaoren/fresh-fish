# python's object model distinguishes between class and instances variables.


# class variables: they are not tied to any particular instance of a class. 
# instead, class variabls store their contents on the class itself, and all objects 
# created from a particular class share access to the  same set of class variables.

class JiGong:
    hobbies = 'buddha'

    def __init__(self, name):
        self.who = name

if __name__ == '__main__':
    luck = JiGong('xiuyuan')
    taiz = JiGong('daoji')

    print('who: ', luck.who, taiz.who)

    print('hobbies: ', luck.hobbies, taiz.hobbies)
