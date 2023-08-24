# 다섯 개의 정수를 하나씩 입력받아서 그 정수들 중에서 가장 큰 값을 출력하시오.


num = int(input("정수를 입력하시오. :"))
max = num

loop_count = 1

while loop_count <= 4:
    num = int(input("정수를 입력하시오. :"))
    if num > max:
        max = num
    loop_count += 1

print("가장 큰 값 : ", max)
