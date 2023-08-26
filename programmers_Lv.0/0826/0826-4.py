# 원소들의 곱과 합
# 정수가 담긴 리스트 num_list가 주어질 때, //모든 소들의 곱이// 모든 원소들의 합의 제곱//보다 작으면 1을
# 크면 0을 return하도록 solution 함수를 완성해주세요.

# map 함수 : 하나씪 꺼내고 계산하고 하나씩 반환
# redude 함수 : 누적으로 계산
# filter 함수 : 참 거짓

from functools import reduce


def solution(num_list):
    j = sum(num_list) * sum(num_list)
    k = reduce(lambda x, y: x * y, num_list)

    if j > k:
        return 1
    else:
        return 0


def solution(num_list):
    s = sum(num_list) ** 2
    m = eval("*".join([str(n) for n in num_list]))
    return 1 if s > m else 0


def solution(num_list):
    a = 1
    b = 0
    for x in num_list:
        a *= x
        b += x
    if a < b * b:
        return 1
    return 0
