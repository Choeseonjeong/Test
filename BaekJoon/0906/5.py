# n : 수열 a
# x : x보다 작은 수 return


def solution(n, x, arr):
    a = []
    for i in arr:
        if i < x:
            a.append(str(i))
    return " ".join(a)


n, x = map(int, input().split(" "))
arr = map(int, input().split(" "))


print(solution(n, x, arr))
