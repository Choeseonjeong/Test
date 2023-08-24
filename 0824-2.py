# -*- coding: utf-8 -*-


# input 함수를 이용하여 원의 반지름을 입력받는다.
# 입력받은 반지름으로 원의 넒이와 원의 둘레를 구하여 소수 셋째 자리까지 출력하는 프로그램을 작성하시오.
# 원주율은 3.141592로 한다.

r = int(input("input radious : "))
print("radious : ", r)

pi = 3.141592

circle_area = r * pi * r
circle_round = r * pi * 2

circle_area = round(circle_area, 3)
circle_round = round(circle_round, 3)

print("원의넓이 : ", circle_area)
print("원의 둘레 : ", circle_round)
