# record, provide named fields 
# 

if __name__ == '__main__':
    ## dict, also called maps or associative arrays 
    ## there's little protection against misspelled field names.
    ## be a trade-off to be made between convenience and error resilience.
    gods = {
        'cui': 'marriage',
        'cox': True,
        'grade': -1,
    }
    print('simple data object: [dict]: ', gods)
