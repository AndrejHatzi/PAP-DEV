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

def table_analysis(toEval, Kvars, indexing):
    table_index = 0
    values = toEval.split(',')
    with open('config/config.init', 'r') as f:
        filedata = f.read()
        for line in f:
            cmng = line.split(' ')
            if cmng[0] == 'current_index':
                table_index = cmng[2]
                filedata = filedata.replace('current_index = {}'.format(str(table_index)), 'current_index = {}'.format(str(table_index + 1)))
                with open('config/config.init', 'w') as f:
                    f.write(filedata)
    _db_header[indexing] = ['@{}'.format(str(table_index + 1))] #Falta Implementar ==> Index Memory
    print(_db_header)
    print(_db_values)
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

#
#with open('file.txt', 'r') as file :
#  filedata = file.read()

# Replace the target string
#filedata = filedata.replace('ram', 'abcd')

# Write the file out again
#with open('file.txt', 'w') as file:
#  file.write(filedata)

def table_append_analysis(line, Kvars, indexing):
    gate = line.index("(") + 1
    backdoor = line.index(")")
    toEval = line[gate:backdoor]
    values = toEval.split(',')
    _db_values[_db_header[indexing][0]] = [] #Creates a empty list
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
        elif 'key=' in (values[i]):
            pass
        else:
            pass

        _db_values[_db_header[indexing][0]].append(values[i])
    strln = indexing + ' '
    #print(values)
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

    print(_db_header)
    print(_db_values)
