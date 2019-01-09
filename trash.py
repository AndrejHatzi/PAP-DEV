import re
my_dict = {
    "var2" : [17, 'integer'],
    "my_number" : ['89', 'string'],
    "my_string" : ['Hello World', 'string'],
    'random_number' : [90.1, 'float'],
    'isTrue' : ['TRUE', 'boolean']
}
var_test = ("var1 = ( 'Sophocles ', 'Herodotus ', my_string )")
#var_test = ("var1 = (7 * 8 + random_number )")


#gate = var_test.index("(") + 1
#backdoor = var_test.index(")")
#cString = var_test[gate:backdoor]
#for K in my_dict:
#    if (re.search(r'{}'.format(K), cString)):
#        cString = cString.replace(" " + K + " ", str(my_dict[str(K)][0]))

#values = cString.split(',')
#print(values)
#cString = ''.join(values)
#print(cString)

gate = var_test.index("(") + 1
backdoor = var_test.index(")")
cString = var_test[gate:backdoor]

#print(values)
toAnalyse = var_test.split(' ')
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
                        print('Error 2" on line');
                except:
                    print('Error 1" on line');

            elif ('"') in values[e]:
                try:
                    cp = values[e].index("'")
                    try:
                        cpp = values[e][cp+1:].index("'")
                        strln += values[e][cp+1:cpp-1]
                    except:
                        print('Error 2" on line')
                except:
                    print('Error 1" on line')
            else:
        #print('Error var not defined or " not in concat call')
                strln += values[e]
    my_dict[toAnalyse[0]] = [strln, 'string']
elif ('"' not in cString) or ("'" not in cString):
    try:
        EqualSignIndex = var_test.index('=')
        cString = var_test[EqualSignIndex+1:]
        cString = cString.replace(' ', '')
        #print('@t', cString)
    except:
        pass
    for K in my_dict:
        #print(K)
        if (re.search(r'{}'.format(K), cString)):
            #print('@b')
            cString = cString.replace(K, str(my_dict[str(K)][0]))
        #print('@a', cString)
    hh = eval(str(cString))
    my_dict[toAnalyse[0]] = hh #Para o body, retirar da func , eh atrbr d var
        #print('Raise Error N6')
else:
    print('Raise Error N7')

print(my_dict)

'''
    if values[e] in my_dict:
        values[e] = my_dict[values[e]][0]
    else:
        pass
    try:
        values[e] = values[e].replace('"', '')
    except:
        pass
    try:
        values[e] = values[e].replace("'", "")
    except
        pass
cString = ''.join(values)
print(cString)
;
toAnalyse = var_test.split(' ')
EqualSignIndex = var_test.index('=')
if ('=' in toAnalyse[1]):
    cString = var_test[EqualSignIndex+1:]

            if ('"' in cString) or ("'" in cString):
                possible_strings = cString.split('+')
                print('@b', possible_strings)
                for i in range(len(possible_strings)):
                    try:
                        possible_strings[i] = possible_strings[i].replace("'", '')
                    except:
                        pass
                    try:
                        possible_strings[i] = possible_strings[i].replace('"', '')
                    except:
                        pass
                    try:
                        possible_strings[i] = possible_strings[i].replace('+', '')
                    except:
                        pass
                    try:
                        possible_strings[i] = possible_strings[i].rstrip()
                    except:
                        pass
                    try:
                        possible_strings[i] = possible_strings[i].lstrip()
                    except:
                        pass
                cString = ''.join(possible_strings)
                print('@f',possible_strings)
                print('@t', cString)

                try:
                    cString = cString.replace('"', '')
                except:
                    cString = cString.replace("'", '')
                try:

                except:
                    pass
            else:
                pass
    print(cString)
my_dict = {
    "var2" : [17, 'integer'],
    "my_number" : ['89', 'string'],
    "my_string" : ['Hello World', 'string'],
    'random_number' : [90.1, 'float'],
    'isTrue' : ['TRUE', 'boolean']
}
q = sum("Hello", 'world')
print(q)
#analyse = ("var1 = (( var2 + 1 + 9.7 - 1 ) / random_number ) * 5 + var2 ");
analyse = ("b = my_string + ', again' ")
toAnalyse = analyse.split(' ')
EqualSignIndex = analyse.index('=')
if ('=' in toAnalyse[1]):
    cString = analyse[EqualSignIndex+1:]
    for K in my_dict:
        if (re.search(r'{}'.format(K), cString)):
            cString = cString.replace(" " + K + " ", str(my_dict[str(K)][0]))
#----------------------------------------------------------------------------
basename = os.path.basename(logfile) => this has not been implemented yet
if basename.endswith('.txt'):
    basename = os.path.splitext(basename)[0]

with open('myfile.txt') as myfile:
     if 'String' in myfile.read():
         print('Blahblah')

#-----------------------------------------------------------------------------

#print(len(my_dict))
#for m in my_dict:
    #print(m)
phrase = ("var1 = (( var2 + 1 + 9.7 - 1 ) / random_number ) * 5 + var2 ");
toAnalyse = phrase.split(' ');
EqualSignIndex = phrase.index('=')
if ('=' in toAnalyse[1]):
    cString = phrase[EqualSignIndex+1:]
    #print(cString)
    for K in my_dict:
        #print(K)
        if (re.search(r'{}'.format(K), cString)):
            cString = cString.replace(" " + K + " ", str(my_dict[str(K)]))
            #print(cString)
    hh = eval(str(cString))
    my_dict[toAnalyse[0]] = hh
        #print('Raise Error')
'''
#print(my_dict)
