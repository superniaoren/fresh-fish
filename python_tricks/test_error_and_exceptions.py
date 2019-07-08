## deal with errors and exceptions 
import sys

class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass


if __name__ == '__main__':
    #ex_a = 10 * (1 / 0)

    while True:
        try:
            x = int(input('Pls enter a number: '))
            break
        except ValueError:
            print('Oops! Invalid number. Try again... ')

    # NOTE: A <= B <= C, means each cls always match A
    for cls in [A, B, C]:
        try:
            raise(cls)
        except C:
            print('C')
        except B:
            print('B')
        except A:
            print('A')
        except:
            print('Unexpected error !! ???')
            print('the default except subexp. can be view as asterisk wildcard')
            print('IT IS a DANGEROUS usage !!!')
        else:
            print('as U use the raise method, the branch would be never reached')    

    
    try:
        fh = open('error_except.txt', 'wt')
        fh.writelines('error and exception procession')
    except OSError as oerr:
        print('OS error: {}'.format(oerr))
    except ValueError:
        print('a common error, error in data procession')
    except:
        print('Unexpected error: ', sys.exc_info()[0])
        raise
