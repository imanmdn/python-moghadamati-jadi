import random
a = 1
z = 99
hads = random.randint(a,z)
print(hads)
javab = (input(' aya dorost ast? bozorgtar= b kochektar= k dorost= d  :   '))

while True:
    if javab == 'd':
        print(' hoooraaa!!!, adade entekhabi shoma  >>', hads , '<<  ast.')
        break
    elif javab == 'k':
        z = hads-1
        hads = random.randint(a,z)
        print(hads)
        javab = (input(' aya dorost ast? bozorgtar= b kochektar= k dorost= d  :   '))

    elif javab == 'b':
        a = hads+1
        hads = random.randint(a,z)
        print(hads)
        javab = (input(' aya dorost ast? bozorgtar= b kochektar= k dorost= d  :   '))