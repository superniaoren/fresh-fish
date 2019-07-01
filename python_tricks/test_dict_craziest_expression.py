#

class AlwaysEqual:
    def __eq__(self, some):
        return True

    def __hash__(self):
        return id(self)

class AlwaysConflict:
    def __hash__(self):
        return 1

class AlwaysSame:
    def __eq__(sefl, some):
        return True

    def __hash__(self):
        return 1

if __name__ == '__main__':
    descrp = 'In python, the keys: $True == 1 == 1.0, ' \
             'The dict conflict happens in key or value, need double check. '
    print(descrp)

    error_prone = {True: 'true?', 1: '1?', 1.0: '1.0?'}
    print(error_prone)

    print('Now, to dig the reason !!')

    key_eq = True == 1 == 1.0
    print('key_eqaul: {}'.format(key_eq))
    print("The boolean type is a subtype of the integer type, and boolean \n"\
          "values behave like the values 0 and 1, respectively, in almost \n"\
          "all contexts, the exception being that when converted to a string,\n"\
          " the strings 'False' or 'True' are returned, respectively.")
    no_yes = ['no', 'yes']
    print("['no', 'yes'][False] = {}".format(no_yes[True]))
    print("['no', 'yes'][True] = {}".format(no_yes[False]))  # 1.0 float not work here

    # overwritten, __eq__ or hash conflict ??  find it!
    print("Find out: ")
    objects = [AlwaysEqual(),
               AlwaysEqual(),
               AlwaysEqual(),
             ]
    print([hash(obj) for obj in objects])
    print(objects[0] == 43)
    print(objects[1] == 'shop on line')
    print(objects[2] == AlwaysEqual())

    print("Test if the keys are overwritten: ")
    key_over = {AlwaysEqual(): 'yes', AlwaysEqual(): 'no'}
    print('key_overwritten: {}'.format(key_over)) # use is? not __eq__ ??
    print('the keys get overwritten effect IS NOT based on their equality comparison result alone')

    print("Test if the hash values are overwritten: ")
    a_conf = AlwaysConflict()
    b_conf = AlwaysConflict()
    print(a_conf == b_conf)
    print("hash = {0}, {1}".format(hash(a_conf), hash(b_conf)))
    value_over = {AlwaysConflict(): 'yes', AlwaysConflict(): 'no'}
    print("value_overwritten: {}".format(value_over))
    print('the keys get overwritten effect IS NOT caused by hash value collisions alone either')
        
    print("Test if the equality && hash-value collisions result in overwritten: ")
    a_same = AlwaysSame()
    b_same = AlwaysSame()
    kv_over = {AlwaysSame(): 'yes', AlwaysSame(): 'no'}
    print(a_same == b_same)
    print("hash = {0}, {1}".format(hash(a_same), hash(b_same)))
    print("kv_overwritten: {}".format(kv_over))

    
