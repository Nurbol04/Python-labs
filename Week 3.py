#1.1
print(4, 8, 15, 16, 23, 42, sep=" ")

#1.2
print(4, 8, 15, 16, 23, 42, sep='\n')

#1.3
x = int(input())
print(x, x+1, x+2, sep='\n')

#1.4
y = int(input())
a = int(input())
b = int(input())
y += a+b
print(y)

#1.5
r = int(input())
v = r ** 3
s = 6 * r ** 2
print("Volume =", v)
print("Total surface area =", s)

#2.1
n = int(input())
k = int(input())
print(k // n, k % n, sep="\n")

#2.2
f = int(input())
print("The digit in the thousands position is ", f // 1000)
print("The number in the hundreds position is ", (f // 100) % 10)
print("The digit in the tens position is ", (f//10) % 10)
print("The digit in the position of units is ", f % 10)

#2.3
p = int(input())
print((p + 1) // 2)
