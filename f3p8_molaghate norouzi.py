x = input().split()

x = [int(num) for num in x]

x.sort()

a = x[1] - x[0]
b = x[2] - x[1]

print(a+b)