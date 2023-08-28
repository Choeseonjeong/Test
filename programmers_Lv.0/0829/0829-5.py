# 피자 나눠 먹기 (1)
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.
# 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.


# 7의 배수 / 몫 구하기 나눠서


def solution(n):
    return (n // 7) + (1 if n % 7 != 0 else 0)


# if 구문 사용하기 위해서는 무조건 else 사용


# def solution(n):
#   return (n - 1) // 7 + 1

# main
n = int(input())
print(solution(n))
