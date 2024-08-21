s1 = -1
s2 = -1
sen = 0
while sen != -1:
    sen = int(input())
    if sen > s1:
        s2 = s1
        s1 = sen
    elif sen > s2:
        s2 = sen
    

print(s1,s2)