# 1
c = list(map(int, input("Enter c: ").split(',')))
b = list(map(int, input("Enter b: ").split(',')))
d = [x for x in c if x not in b]
print(d)

# 2
# C:\Users\Nurbol\PycharmProjects\pythonProject3
import os

e = input(r"Path to folder: ")
print(f"Files in the directory: {e}")
files = os.listdir(e)
files = [f for f in files if os.path.isfile(e + '/' + f)]
print(*files, sep="\n")

# 3
s = 0
g = int(input("Task 3: "))
while g > 0:
    s += int(g % 10)
    g = int(g / 10)
print(s)

# 4
h = input("Task 4: ")
count = h.count(',')
print(count)

# 5
i = int(input("Enter i: "))
j = int(input("Enter j: "))
k = i
i = j
j = k
print("i =", i)
print("j =", j)

# 6
l = list(map(int, input("Enter l: ").split(',')))
m = list(filter(lambda x: (x % 15 == 0), l))
print("New list", m)

# 7
n = list(map(int, input("Enter n: ").split(',')))
uniq = len(n) == len(set(n))
print(uniq)
