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

def seekOnFile(file, len_values, values, old_values):
    with open(core_engine['database'], 'r') as f:
        filedata = f.read()

    for i in range(len_values):
        filedata = replace(old_values[i], values[i])

    with open(core_engine['database'], 'w') as f:
        f.write(filedata)



def table_append_analysis(line, Kvars, indexing):
    gate = line.index("(") + 1
    backdoor = line.index(")")
    toEval = line[gate:backdoor]
    values = toEval.split(',')
    _db_values[_db_header[indexing][0]] = []
    for i in range(len(values)):
        try:
            values[i] = values[i].replace(' ', '')
        except:
            pass

        if "'" in (values[i]):
            values[i] = values[i].replace("'", '')

        elif '"' in (values[i]):
            values[i] = values[i].replace('"', '')
        elif values[i] in Kvars:
            values[i] = Kvars[values[i]][0]
            try:
                values[i] = values[i].replace('\n', '')
            except:
                pass
        elif 'key=' in (values[0]):
            pass
        else:
            pass

        _db_values[_db_header[indexing][0]].append(values[i])
    strln = indexing + ' '
    print(values)
    if len(values) == (len(_db_header[indexing]) - 1):
        for i in range(len(values)):
            strln += str(values[i]) + ' '

        handshake = False
        with open(core_engine['databaseValue'], 'r') as f:
            if strln in f.read():
                handshake = True

        if (handshake == True):
            pass
        else:
            with open(core_engine['databaseValue'], 'a') as f:
                f.write(strln)
                f.write('\n')
    else:
        print(errors['error3'])
