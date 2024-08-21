#ÙˆØ±ÙˆØ¯ÛŒ Ù†Ù…ÙˆÙ†Ù‡:
#BaHram
#MaHnaZ

#Ø®Ø±ÙˆØ¬ÛŒ Ù†Ù…ÙˆÙ†Ù‡:
#Bahram
#Mahnaz
def std(a):
    a = a.lower()
    a = a.capitalize()
    return a


asami = []

for i in range(0, 10):
    temp = std(input())
    asami.append(temp)

for j in range(0, 10):
    print(asami[j])