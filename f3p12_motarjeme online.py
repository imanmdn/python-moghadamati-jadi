
from collections import OrderedDict

# خواندن تعداد کلمات دیکشنری
y = int(input())

# ایجاد یک Ordered x برای دیکشنری
x = OrderedDict()

# خواندن دیکشنری
for _ in range(y):
    kalame, tarjome = input().split()
    x[kalame] = tarjome

# خواندن جمله
sentence = input().split()

# ترجمه کردن جمله
translated_sentence = []
for kalame in sentence:
    translated_sentence.append(x.get(kalame, kalame))

# چاپ کردن جمله ترجمه شده
print(' '.join(translated_sentence))