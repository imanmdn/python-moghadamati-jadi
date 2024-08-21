jam = 0
bord = 0

for i in range(1, 31):
    voroodi = int(input())
    jam += voroodi
    if voroodi == 3:
        bord = bord+1

print(jam, '', bord)