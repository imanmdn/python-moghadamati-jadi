x = input()
x = x.lower()
x = x.replace('a','')
x = x.replace('e','')
x = x.replace('i','')
x = x.replace('o','')
x = x.replace('u','')
javab = ''
for i in range(0,len(x)):
    javab =javab+ '.'+x[i]
print(javab)