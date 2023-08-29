a = int(input())
count = 0
sum = 0
while True:
    sum += count
    count += 1
    if sum >= a:
        break

print(sum)
