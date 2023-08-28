# 짝수는 싫어요
# 정수 n이 매개변수로 주어질 때,
# n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.


def solution(n):
    return list([s for s in range(1, int(n) + 1, 2)])


# main
n = input()
print(solution(n))
