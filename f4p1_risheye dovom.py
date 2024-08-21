import math

n = int(input())

x = []

for i in range(n):
    y = int(input())
    y = math.sqrt(y)
    x.append(y)


for j in x:
    eight = (f'{j:.8f}')
    print(eight[:-4])