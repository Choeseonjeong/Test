# list 사용
# score 리스트에 다섯 개의 성적(정수)를 입력 받아서 다음과 같이 출력하시오.
# 성적을 입력받을 때는 반드시 for 구문을 사용하고 파이썬 내장 함수를 적절히 이용하시오.

# 성적을 입력하시오 : 90
# 성적을 입력하시오 : 88
# 성적을 입력하시오 : 75
# 성적을 입력하시오 : 93
# 성적을 입력하시오 : 80

# 입력한 성적들 : [90,88,75,93,80]
# 최고 성적 : 93
# 최저 성적 : 75
# 평균 : 85.20

score = []

for i in range(5):
    x = int(input("성적을 입력하시오 :"))
    score.append(x)
print()
print("입력한 성적들 : ", score)


max = 0
for i in score:
    if max < i:
        max, i = i, max
print()
print("최고 성적 : ", max)

min = 100
for i in score:
    if min > i:
        min, i = i, min
print()
print("최소 성적 : ", min)


avg = 0
score_sum = 0

for i in score:
    score_sum += i
avg = score_sum / 5
print()
print("평균 :", avg)
