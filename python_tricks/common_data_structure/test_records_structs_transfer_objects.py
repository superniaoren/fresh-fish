# record, provide named fields 
# 

if __name__ == '__main__':
    ## dict, also called maps or associative arrays 
    ## there's little protection against misspelled field names.
    ## these properties can introduce surprising bugs.
    ## be a trade-off to be made between convenience and error resilience.
    print('-' * 40, " simple dict ")
    gods = {
        'cui': 'marriage',
        'cox': True,
        'grade': -1,
    }
    print('simple data object: [dict]: ', gods)

    
    print('-' * 40, " immutable tuple ")
    print('\n\n tuple cost less memory than list: ')
    import dis
    print('\n\n constructing a tuple constant SHOULD take a single LOAD_CONST opcode:')
    dis.dis(compile("('mood', 2.1414, true, false)", '', 'eval'))
    dis.dis(compile("('mood', 2.1414, 'true', 'false')", '', 'eval'))
    print('\n\n constructing a list object SHOULD take several LOAD_CONST opcode:')
    dis.dis(compile("['mood', 2.1414, true, false]", '', 'eval'))
    dis.dis(compile("['mood', 2.1414, 'true', 'false']", '', 'eval'))

    
