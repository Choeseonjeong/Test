a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a < b and b < c:
    print(a)
elif a > b and b < c:
    print(b)
else:
    print(c)
