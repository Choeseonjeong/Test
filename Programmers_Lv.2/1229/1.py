# 최솟값 만들기


def solution(A, B):
    answer = 0
    A, B = sorted(A), sorted(B, reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


print(solution([1, 2], [3, 4]))
