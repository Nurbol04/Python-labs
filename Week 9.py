# 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

# 2
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d = []
for s in range(len(c)):
    for q in range(len(b)):
        if c[s] == b[q]:
            d.append(c[s])
print(d)

# 3
import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
ascending = dict(sorted(d.items(), key=operator.itemgetter(1)))
descending = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)

# 4
dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}
dict_d = {}
for d in (dict_a, dict_b, dict_c):
    dict_d.update(d)
print(dict_d)

# 5
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
descending = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)[:3]
print(descending)

# 7
n = int(input("Rows: "))


def t(n):
    t = []

    for p in range(n):
        r = [1] * (p + 1)
        for j in range(1, p):
            r[j] = t[p - 1][j - 1] + t[p - 1][j]

        t.append(r)

    for r in t:
        print(" " * (n - len(r)), end="")
        print(" ".join(map(str, r)))


t(n)

# 6