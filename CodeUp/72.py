a, b, c = input().split()

a, b, c = int(a), int(b), int(c)
count = 0

for i in range(0, a):
    for j in range(0, b):
        for k in range(0, c):
            count += 1
            print(i, j, k)

print(count)
