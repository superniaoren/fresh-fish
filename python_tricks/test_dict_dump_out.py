## print the dictionary elegantly
import json


if __name__ == '__main__':
    # default, print the resulting string 
    xd = {'kaiqi': 'yiyaya', 'turtle': 450, 'new_pants': 365}
    print(str(xd))

    # use json format
    jd = json.dumps(xd, indent=4, sort_keys=True)
    print(jd)
