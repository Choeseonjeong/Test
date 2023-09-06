def solution(x, y):
    if y < 45:
        if x > 0:
            return (x - 1), (60 - 45 + y)
        else:
            return (23), (60 - 45 + y)
    elif y == 45:
        return x, 0

    else:
        return x, 60 - y


x, y = map(int, input().split(" "))


print(solution(x, y))
