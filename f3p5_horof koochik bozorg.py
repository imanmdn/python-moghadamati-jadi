x = input()

def tatbigh():
    bozorg = 0
    koochik = 0
    for i in range(len(x)):
        if x[i].isupper():
            bozorg += 1
        elif x[i].islower():
            koochik += 1
    return bozorg, koochik

bozorg, koochik = tatbigh()

if koochik >= bozorg:
    x = x.lower()
else:
    x = x.upper()

print(x)