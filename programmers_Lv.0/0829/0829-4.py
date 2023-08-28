# 짝수 홀수 개수
# 정수가 담긴 리스트 num_list가 주어질 때,
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.


def solution(num_list):
    count = 0
    counts = 0
    for i in num_list:
        if i % 2 == 0:
            count += 1
        else:
            counts += 1
    return count, counts


# main
num_list = [1, 2, 3, 4, 5]
print(solution(num_list))
