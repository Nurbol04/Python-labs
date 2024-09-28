# 0
a = float(input())
b = float(input())
o = input()
match o:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)

# 1
f = int(input())
c = (f // 1000) + (f % 10)
g = abs(((f // 100) % 10) - ((f // 10) % 10))
if c == g:
    print("yes")
else:
    print("no")

# 2
d = int(input())
if d >= 18:
    print("Access is allowed")
else :
    print("Access denied")

# 3
e = int(input())
f = int(input())
h = int(input())
if abs(e-f) == abs(f-h):
    print("yes")
else:
    print("no")

# 6
i = int(input())
k = int(input())
l = int(input())


