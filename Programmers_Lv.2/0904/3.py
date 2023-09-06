# 모험가 길드


data = input().split(" ")

count = 0  # 현재 그룹에 포함된 모험가의 수
result = 0  # 그룹의 수

data.sort()
print(data)


for i in range(len(data)):
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
