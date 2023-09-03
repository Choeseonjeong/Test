# 카운트 다운
# 정수 start_num와 end_num가 주어질 때,
# start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.


def solution(start, end_num):
    num_list = []
    for i in range(start, end_num - 1, -1):
        num_list.append(i)
    return num_list


def solution(start, end):
    return [i for i in range(start, end - 1, -1)]


# main
start = int(input())
end_num = int(input())
print(solution(start, end_num))
