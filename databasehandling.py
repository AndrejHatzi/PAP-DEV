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
            if values[i] in Kvars:
                values[i] = Kvars[values[i]][0]
        _db_header[indexing].append(values[i])


def table_append_analysis(line, Kvars, indexing):
    gate = line.index("(") + 1
    backdoor = line.index(")")
    toEval = line[gate:backdoor]
    values = toEval.split(',')
    _db_values[_db_header[indexing][0]] = []
    for i in range(len(values)):
        try:
            values[i] = values[i].replace(' ', '')
            values[i] = value[i].replace('\n', '')
            #name = name.rstrip('\n')
        except:
            pass
        if "'" in (values[i]):
            values[i] = values[i].replace("'", '')

        elif '"' in (values[i]):
            values[i] = values[i].replace('"', '')
        else:
            if values[i] in Kvars:
                values[i] = Kvars[values[i]][0]
        _db_values[_db_header[indexing][0]].append(values[i])
    print(len(values))
    print('@t',len(_db_header[indexing]))
    strln = ''
    if len(values) == (len(_db_header[indexing]) - 1):
        for i in range(len(values)):
            strln += str(values[i]) + ' '
        print(values)
        print(strln)
        with open(core_engine['databaseValue'], 'a') as f:
            f.write('\n')
    else:
        print(errors['error3'])
        #with open(core_engine['databaseValue'], 'a') as f:
