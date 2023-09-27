# 소수 찾기
from itertools import permutations


def is_prime_numbers(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    a = []
    answer = 0
    for i in range(len(numbers)):
        a.extend(map(int, map("".join, permutations(list(numbers), i + 1))))
    a = list(set(a))
    for i in a:
        if is_prime_numbers(i):
            answer += 1

    return answer


# main
print(solution("011"))


# 1,01,10
# 12,102
