from head import function_types, keywords, assign, errors, data_types
from functions import var_evaluation, partial_print_evaluation, deep_var_evaluation, hybrid_var_evaluation
from databasehandling import table_analysis, startDatabase
import re
KontrolFlow = []
Kvars = {
    "init" : ['TRUE', 'boolean'],
    "my_string" : ['otherDbFile', 'string']
}
def iteration(file):
    with open(file) as f:
        for line in f:
            cObject = line.split(' ')
            if (cObject[1] == keywords["variable"]):
                EqualSignIndex = line.index("=") + 2
                toEval = line[EqualSignIndex:]
                #print(toEval)
                #type,valor = var_evaluation(toEval)
                if (cObject[0] in Kvars):
                    Kvars[cObject[0]] = [valor, type]
                    KontrolFlow.append([assign["change_value"], cObject[0], valor])
                else:
                    toEval = line[EqualSignIndex-1:]
                    #Kvars[cObject[0]] = [valor, type]
                    #KontrolFlow.append([assign["assign_var"], cObject[0], valor])
                    value = hybrid_var_evaluation(Kvars, toEval)
                    '''
                    if (value == errors['error2']):
                        pass
                    else:
                        Kvars[cObject[0]] = value
                        KontrolFlow.append([assign["assign_var"], cObject[0], value])
                    '''



            if (cObject[0] == keywords["print"]):
                gate = line.index("(") + 1
                backdoor = line.index(")")
                toEval = line[gate:backdoor]
                valor = partial_print_evaluation(toEval)
                if valor == 0:
                    if (toEval in Kvars):
                        valor = Kvars[toEval][0]
                KontrolFlow.append([assign["print_call"], keywords["print"], valor])

            if (cObject[0] == keywords["start_db"]):
                startDatabase(cObject[1], Kvars)

            if (cObject[0] == keywords["init_table"]):
                gate = line.index("(") + 1
                backdoor = line.index(")")
                toEval = line[gate:backdoor]
                valor = table_analysis(toEval, Kvars, cObject[1])


iteration('exp_db.txt')
print(KontrolFlow)
print(Kvars)
