from head import errors, core_engine


_db_header = {

}

_db_values = {

}
def startDatabase(name, Kvars):
    if (name[0] == '"'):
        name = name.replace('"', '')
        name = name.replace('\n', '')
    elif (name[0] == '"'):
        name = name.replace("'", "")
        name = name.replace('\n', '')
    else:
        name = name.replace(' ', '')
        name = name.rstrip('\n')
        if name in Kvars:
            name = Kvars[name][0]
        else:
            print(errors['var_not_found'])


    name = name + '{}'.format('.db')
    core_engine['databaseValue'] = name
    with open(name, 'a') as f:
        pass
#d[year].append(month)
def table_analysis(toEval, Kvars, indexing):
    values = toEval.split(',')
    _db_header[indexing] = ['@2']
    for i in range(len(values)):
        try:
            values[i] = values[i].replace(' ', '')
        except:
            pass
        if "'" in (values[i]):
            values[i] = values[i].replace("'", '')

        elif '"' in (values[i]):
            values[i] = values[i].replace('"', '')
        else:
            pass
        _db_header[indexing].append(values[i])
    print(_db_header)
            #if name in Kvars:



    print(values)
