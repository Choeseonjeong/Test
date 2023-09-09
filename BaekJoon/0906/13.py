def solution(numbers):
    n = list(map(str, numbers))
    n.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(n)))


# main
numbers = list(map(int, input().split(",")))
print(solution(numbers))


# 정렬 - 가장 큰 수
# 못품
# 숫자를 12,112면 121212,112112로 만들어서 비교함
