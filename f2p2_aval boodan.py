x = int(input())
a = 0

for i in range(1, x):
    if x % i == 0:
        a = a+1

if a == 1:
    print("prime")
else:
    print("not prime")