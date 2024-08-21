a = input()

# Find all occurrences of AB and BA in the input
AB_positions = []
BA_positions = []

for i in range(len(a) - 1):
    if a[i:i+2] == 'AB':
        AB_positions.append(i)
    elif a[i:i+2] == 'BA':
        BA_positions.append(i)

# Check if there are any non-overlapping occurrences
for ab_pos in AB_positions:
    for ba_pos in BA_positions:
        if abs(ab_pos - ba_pos) > 1:
            print('YES')
            exit()

print('NO')