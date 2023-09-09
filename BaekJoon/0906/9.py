n, k = map(int, input().split(" "))
count = 0
a = []
for i in range(n):
    num = int(input())
    a.append(num)

a.sort()

for coin in a:
    if k >= coin:
        count += k // coin
        k %= coin

print(count)
