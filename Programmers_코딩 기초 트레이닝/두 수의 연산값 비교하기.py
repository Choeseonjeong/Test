def solution(a, b):
    if int(str(a) + str(b)) == 2 * a * b:
        return int(str(a + b))
    else:
        return max(int(str(a) + str(b)), 2 * a * b)


print(solution(2, 91))
