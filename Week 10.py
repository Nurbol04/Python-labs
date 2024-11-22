# 1
s = input()


def Palindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


ans = Palindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# 2
s = int(input())


def sec(s):
    day = s // (24 * 3600)
    s = s % (24 * 3600)
    hour = s // 3600
    s %= 3600
    minutes = s // 60
    s %= 60
    seconds = s
    print(day, "days", hour, "hours",
          minutes, "minutes",
          seconds, "seconds")


sec(s)

# 3
sequence = input("Enter numbers: ")
l = sequence.split(",")
t = tuple(l)
print("List:", l)
print("Tuple:", t)

# 4
a = input("Enter: ")
c = list(a)
print(c[0])
print(c[-1])


# 5
def extension(f_name):
    try:
        ex = f_name.split('.')[-1]
        if ex == f_name:
            raise ValueError("No extension")
        return ex
    except Exception as e:
        return f"Error: {str(e)}"


file_name = input("File name: ")
print(f"File extension: {extension(file_name)}")

# 6
n = int(input("Enter n: "))
d = str(n)
n1 = d + d
n2 = d + d + d
v = n + int(n1) + int(n2)
print("Value: ", v)


# 7
def e():
    g = list(map(int, input("Enter list: ").split(',')))

    for num in g:
        if num == 237:
            print(num)
            break
        elif num % 2 == 0:
            print(num)


e()
