from head import function_types, keywords, assign
from functions import var_evaluation, partial_print_evaluation
KontrolFlow = []
Kvars = {
    "init" : 'TRUE',
}
def iteration(file):
    with open(file) as f:
        for line in f:
            cObject = line.split(' ')
            if (cObject[1] == keywords["variable"]):
                EqualSignIndex = line.index("=") + 2
                toEval = line[EqualSignIndex:]
                type,valor = var_evaluation(toEval)
                if (cObject[0] in Kvars):
                    Kvars[cObject[0]] = [valor, type]
                    KontrolFlow.append([assign["change_value"], cObject[0], valor])
                else:
                    Kvars[cObject[0]] = [valor, type]
                    KontrolFlow.append([assign["assign_var"], cObject[0], valor])

            if (cObject[0] == keywords["print"]):
                gate = line.index("(") + 1
                backdoor = line.index(")")
                toEval = line[gate:backdoor]
                valor = partial_print_evaluation(toEval)
                if valor == 0:
                    if (toEval in Kvars):
                        valor = Kvars[toEval][0]
                KontrolFlow.append([assign["print_call"], keywords["print"], valor])


iteration('script.txt')
print(KontrolFlow)
print(Kvars)
