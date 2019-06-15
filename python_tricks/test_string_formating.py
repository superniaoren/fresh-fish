import dis
import time
from string import Template

PRIVATE_KEYS='confidential'

def greet(name, question, style=0):
    # literal string interpolation, most recommended
    if style == 0:
        return f"Hello, {name:s}, a quick question {question}?"
    elif style == 1:
        return ('Heelo, ', name, 'a quick question ', question, '?')
    # new style string formatting
    elif style == 2:
        error = 12450
        return('Heeelo, {nm}, a quick question {qt:s}? style={st:d}, errrono={er:x}'.format(nm=name, qt=question, st=style, er=error))
        #return('Heeelo, {nm}, a quick question {qt:s}? style={st:d}, errrono={er:#x}'.format(nm=name, qt=question, st=style, er=error))
    # old style string formatting
    elif style == 3:
        return('Heeelo, %(nm)s, a quick question %(qt)s? style=%(st)d' % {"nm":name, 'qt':question, 'st':style})
        #return('Heeelo, %s, a quick question %s? style=%d' % (name, question, style))
    elif style == 4:
        # template not support format specifiers
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        temp = Template('Heeeelo, $name, a quick question $question? style=$style, timestamp=$timestamp')
        stemp = temp.substitute(name=name, question=question, style=style, timestamp=timestamp)
        return stemp

class Error:  
    def __init__(self):
        #print(self.__globals__[PRIVATE_KEYS])
        pass

if __name__ == '__main__':
    name = 'gooloo'
    question = 'are you a blue cat'

    style = 0
    gt = greet(name, question, style)
    print(gt)

    style = 2
    gt = greet(name, question, style)
    print(gt)

    style = 3
    gt = greet(name, question, style)
    print(gt)

    style = 4
    gt = greet(name, question, style)
    print(gt)

    #dis.dis(greet)

    err = Error()
    malicious = '{error.__init__.__globals__[PRIVATE_KEYS]}'
    safe_input = '${error.__init__.__globals__[PRIVATE_KEYS]}'
    print(malicious.format(error=err))
    print(Template(safe_input).substitute(error=err))
