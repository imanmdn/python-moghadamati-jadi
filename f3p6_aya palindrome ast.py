def iman(x, w):
    count = 0
    for i in range(w):
        if x[i] == x[-(i+1)]:
            count += 1
    if count == w:
        return "palindrome"
    else:
        return "not palindrome"

x = input().lower()
y = len(x)

if y % 2 == 0:
    w = y // 2
    result = iman(x, w)
else:
    w = (y - 1) // 2
    result = iman(x, w)

print(result)