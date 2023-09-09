def solution(s):
    s = list(map(int, s.split(" ")))
    return str(min(s)) + " " + str(max(s))


# main
k = input().split()
print(solution(k))
