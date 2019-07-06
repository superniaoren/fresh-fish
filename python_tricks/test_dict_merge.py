# merge dictionaries 
# a common use case is to overridden the default dict with input

if __name__ == '__main__':
    xd = {'cat': 3.5, 'tumor': 4}
    yd = {'tumor': 'cancer', 'hit': True}
    print('xd: {}'.format(xd))
    print('yd: {}'.format(yd))
    
    # 1, classic solution: use built-in dictionary update() method: 
    zd = {}
    zd.update(xd)
    zd.update(yd)
    print('zd: {}'.format(zd))

    # naive imple. of update() method might look like this:
    def update(dict_dst, dict_src):
        for key, value in dict_src.items():
            dict_dst[key] = value

    sd = {}
    update(sd, xd)
    update(sd, yd)
    print('sd: {}'.format(sd))

    # 2, use dict() built-in combind with the **-operator, to unpack the dictionary 
    td = dict(xd, **yd)
    print('td: {}'.format(td))

    # 3, for python >= 3.5, merge from left to right
    ud = {**xd, **yd, **sd}
    print('ud: {}'.format(ud))
    
    
