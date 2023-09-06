# 같은 숫자는 싫어


# def solution(arr):
#     a = []
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i - 1]:
#             a.append(arr[i - 1])

#     return a


def solution(arr):
    a = []
    for i in arr:
        if len(a) == 0 or a[-1] != i:  # 오호 리스트와 직접 비교하네
            a.append(i)
    return a


# main
arr = input().split(",")
arr = input().split(",")
print(solution(arr))
