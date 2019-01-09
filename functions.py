from head import data_types
from head import errors
import re

def var_evaluation(cObject):
    if (cObject[0] == '"') or (cObject[0] == "'"):
        if (cObject[0] == '"'):
            type = cObject.replace('"', '')
        elif (cObject[0] == "'"):
            type = cObject.replace("'", "")
        return data_types["string"], type
    elif ('.' in str(cObject)):
        type = cObject
        return data_types["float"], float(type)
    elif (cObject.strip() == 'TRUE') or (cObject.strip() == 'FALSE'):
        type = cObject
        return data_types["boolean"], type
    else:
        type = cObject
        return data_types["integer"], int(type)

def deep_var_evaluation(Kvars, toEval):
    for K in Kvars:
        if (re.search(r'{}'.format(K), toEval)):
            toEval = toEval.replace(" " + K + " ", str(Kvars[K]))
    try:
        toEval = eval(str(toEval))
        return toEval
    except:
        return errors['error2']

def hybrid_var_evaluation(Kvars, toEval):
    print('@t', toEval)
    for K in Kvars:
        if (re.search(r'{}'.format(K[0]), toEval)):
            toEval = toEval.replace(" " + K + " ", str(Kvars[K][0]))

    print(toEval.strip())
    return(toEval.strip())


##Under Contruction##
def continuous_var_evaluation(Kvars, line, lindex):
    gate = line.index("(") + 1
    backdoor = line.index(")")
    cString = line[gate:backdoor]
    toAnalyse = line.split(' ')
    if ('"' in cString) or ("'" in cString):
        for K in my_dict:
            if (re.search(r'{}'.format(K), cString)):
                cString = cString.replace(" " + K + " ", str(my_dict[str(K)][0]))
            values = cString.split(',')
            strln = ''
            for e in range(len(values)):
                if ("'") in values[e]:
                    try:
                        cp = values[e].index("'")
                        try:
                            cpp = values[e][cp+1:].index("'")
                            strln += values[e][cp+1:-1]
                        except:
                            print('Error 2" on line', lindex);
                    except:
                        print('Error 1" on line', lindex);

                elif ('"') in values[e]:
                    try:
                        cp = values[e].index("'")
                        try:
                            cpp = values[e][cp+1:].index("'")
                            strln += values[e][cp+1:cpp-1]
                        except:
                            print('Error 2" on line', lindex)
                    except:
                        print('Error 1" on line', lindex)
                else:
                    strln += values[e]
        return (strln, data_types['string'])
        #my_dict[toAnalyse[0]] = [strln, 'string']
    elif ('"' not in cString) or ("'" not in cString):
        try:
            EqualSignIndex = var_test.index('=')
            cString = var_test[EqualSignIndex+1:]
            cString = cString.replace(' ', '')
        except:
            pass
        for K in my_dict:
            if (re.search(r'{}'.format(K), cString)):
                cString = cString.replace(K, str(my_dict[str(K)][0]))
        try:
            value = eval(str(cString))
        except:
            pass
        type, num_value = var_evaluation(value)
        return (type, num_value)
        #my_dict[toAnalyse[0]] = hh #Para o body, retirar da func , eh atrbr d var
    else:
        print('Raise Error N7', lindex)

    print(my_dict)

def partial_print_evaluation(cObject):
    print(cObject)
    if (cObject[0] == '"'):
        valor = cObject.replace('"', '')
        return valor
    elif (cObject == "'"):
        valor = cObject.replace("'", "")
        return valor
    else:
        valor = 0
        return valor
