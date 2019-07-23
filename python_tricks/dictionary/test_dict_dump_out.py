## print the dictionary elegantly
import json
import pprint


# pprint is the recommended method
if __name__ == '__main__':
    # default, print the resulting string 
    xd = {'kaiqi': 'yiyaya', 'turtle': 450, 'new_pants': 365}
    print(str(xd))

    # use json format
    # NOTE: be sure the $xd is free of non-primitive data types
    jd = json.dumps(xd, indent=4, sort_keys=True)
    print(jd)

    # pprint 
    pd = {'mumu': jd, 'woohoo': 3.1415926545327558, 'morning': 'haloha'}
    pprint.pprint(pd)
