import re

my_dict = {
    "var2" : 17,
    "my_number" : '89',
    "my_string" : '"Hello World"',
    'random_number' : 90
}

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

#print(my_dict)
