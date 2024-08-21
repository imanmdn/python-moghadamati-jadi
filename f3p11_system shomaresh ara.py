from collections import OrderedDict

n = int(input())
countries = OrderedDict()

for _ in range(n):
    country = input()
    countries[country] = countries.get(country, 0) + 1

sorted_countries = sorted(countries.items())

for country, count in sorted_countries:
    print(country, count)