def maghsoom(x):
    count = 0
    for i in range(1, x + 1):
        if (x % i) == 0:
            count += 1
    return count

max_number = 0
max_count = 0

for _ in range(20):
    adad = int(input())
    count = maghsoom(adad)
    if count > max_count:
        max_count = count
        max_number = adad
    elif count == max_count and adad > max_number:
        max_number = adad

print(max_number, max_count)