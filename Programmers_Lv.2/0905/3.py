# 1이 될 때까지

n, k = map(int, input().split())

result = 0

count = 0


while n >= k:
    if n % k == 0:
        n = n / k
        count += 1
    else:
        n = n - 1
        count += 1
    result = count
print(result)
