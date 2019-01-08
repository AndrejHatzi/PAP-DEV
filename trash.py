import re

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
basename = os.path.basename(logfile)
if basename.endswith('.txt'):
    basename = os.path.splitext(basename)[0]

with open('myfile.txt') as myfile:
     if 'String' in myfile.read():
         print('Blahblah')











#-----------------------------------------------------------------------------


#print(len(my_dict))
#for m in my_dict:
    #print(m)
'''
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
'''
