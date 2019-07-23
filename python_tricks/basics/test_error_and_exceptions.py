## deal with errors and exceptions 
import sys

class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

class Error(Exception):
    pass

class NameError(Error):
    def __init__(self, descrp):
        self.expression = descrp

    def __repr__(self):
        return self.expression

class InputErorr(Error):
    """
    exception raised for errors in the input
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


if __name__ == '__main__':
    # 1
    while True:
        try:
            x = int(input('Pls enter a number: '))
            break
        except ValueError:
            print('Oops! Invalid number. Try again... ')

    # 2, NOTE: A <= B <= C, means each cls always match A
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

    # 3, use else branch 
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
    else:
        fh.close()

    try:
        raise Exception('premature', 'death')
    except Exception as inst:
        print(type(inst))   # the exception class
        print(inst.args)    # args stored in .args
        print(inst)         # __str__ allows .args to be printed direct
                            # but could be overridden in exception subclasses
        x, y = inst.args
        print('exception.args[0] = ', x)
        print('exception.args[1] = ', y)

    # 4, zero-div exception
    try:
        ex_a = 10 * (1 / 0)
    except ZeroDivisionError as err:
        print(type(err))
        print('handling error: ', err) 

    # 5, raise NameError('Reach here ...')
    hithere = NameError('Reach here ...')
    print('Reach: {}'.format(hithere))

    try:
        raise NameError('throw an exception: NameError')
    except NameError:
        print('an exception flew by.')
        raise   # NOTE: throw exception after the finally clause 
    finally:
        print('first excuting the finally clause')
        print('and then throw the exception after -finally- clause')
        print('NOTE: finally-clause often used to be the resource collector')



