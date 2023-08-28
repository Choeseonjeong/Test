# 배열의 평균값

# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

# 파이썬에는 avg함수가 없음


def solution(numbers):
    return sum([i for i in numbers]) / len(numbers)


# main

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = solution(numbers)
print(k)
