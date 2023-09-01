# 자릿수 더하기
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요.


def solution(n):
    sum = 0
    for i in str(n):  # [0], [1], [2] 등을 한번씩 가는 것
        sum += int(i)
    return sum


# return sum(int(i) for i in str(n))

# main
n = input()
print(solution(n))
k = solution(n)
print(type(k))


# def solution(n):
#    k = int(n[0]) + int(n[1])
#    return k
