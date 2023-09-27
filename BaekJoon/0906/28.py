def solution(numbers):
    n = list(map(str, numbers))
    n.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(n)))


# main
print(solution([3, 30, 34, 5, 9]))
