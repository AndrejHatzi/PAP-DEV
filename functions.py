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
            toEval = toEval.replace(" " + K[0] + " ", str(Kvars[K[0]]))

    print(toEval.strip())
    return(toEval.strip())


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
