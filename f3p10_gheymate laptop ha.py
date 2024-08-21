def sort_key(item):
    return item[0], -item[1]

n = int(input())
laptops = []

for j in range(n):
    price, quality = input().split()
    laptops.append((int(price), int(quality)))

laptops = sorted(laptops, key=sort_key)


happy = False
for i in range(n-1):
    if laptops[i][1] > laptops[i+1][1]:

        happy = True
        break

if happy:
    print("happy irsa")
else:
    print("poor irsa")
        