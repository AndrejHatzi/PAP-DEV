from head import data_types
from head import errors
#from body import Kvars
def var_evaluation(cObject):
    if (cObject[0] == '"') or (cObject[0] == "'"):
        if (cObject[0] == '"'):
            type = cObject.replace('"', '')
        elif (cObject[0] == "'"):
            type = cObject.replace("'", "")
        return data_types["string"], type
    elif ('.' in str(cObject)):
        type = cObject
        return data_types["float"], type
    elif (cObject.strip() == 'TRUE') or (cObject.strip() == 'FALSE'):
        type = cObject
        return data_types["boolean"], type
    else:
        type = cObject
        return data_types["integer"], type

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
