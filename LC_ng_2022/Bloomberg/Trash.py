from collections import Counter

temp = Counter('abcabcababcde')
print(temp)
for num,count in enumerate(dict(temp).items()):
    print(count)

a = {'数学': 95, '语文': 89, '英语': 90}
for key, value in a.items():
    print(key,value)


dict = {('Leyton', 'Waterloo'):[22, 2],('Paradise', 'Cambridge'): [14, 1]}

print(dict)