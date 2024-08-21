y = input()
x = input().split()
x = [int(num) for num in x]
c = 0

for i in range(0,len(x)):
    if x[i] < 3:
        c = c+1
z = c // 3

print(z)