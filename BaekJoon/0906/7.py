# a = {1: 3, 2: 1, 3: 4, 4: 3, 5: 2}
# sum = 0
# b = []
# for i in range(1, n + 1):
#     if i in a:
#         b.append(a[i])

# b.sort()
# print(b)
# sum = 0
# for i in range(len(b)):
#     for j in range(i + 1):
#         sum += b[j]
# print(sum)
#########문제를 잘못봄#########

n = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()

total_time = 0
personal_time = 0
for i in arr:
    personal_time += i
    total_time += personal_time
print(total_time)
