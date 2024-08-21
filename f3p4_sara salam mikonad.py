x = input()

h = x.find('h')
e = x.find('e', h+1)
l_1 = x.find('l', e+1)
l_2 = x.find('l', l_1+1)
o = x.find('o', l_2+1)
if o > l_2 > l_1 > e > h:
    print('YES')
else:
    print('NO')