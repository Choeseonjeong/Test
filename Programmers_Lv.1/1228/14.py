# 같은 숫자는 싫어


def solution(arr):
    a = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            a.append(arr[i])
    return a


print(solution([4, 4, 3]))
