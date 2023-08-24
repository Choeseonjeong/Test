# 하나의 양의 정수를 입력받아서 그 수의 약수를 모두 출력하고 약수의 개수도 출력하시오.


num = int(input("정수를 입력하시오 : "))


# 약수구하는 법 : 1씩 증가한 값을 받은 숫자로 나눠서 나머지가 0인 것


a = 1
count = 0
# 밖에서 정의

while a <= num:
    if num % a == 0:
        print(a)
        count += 1
    a += 1


print("약수의 개수 : ", count)
