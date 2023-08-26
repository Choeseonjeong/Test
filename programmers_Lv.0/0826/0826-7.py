# 마지막 두 원소
# 정수 리스트 num_list가 주어질 때,
# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.


def solution(num_list):
    if int(num_list[-2]) > int(num_list[-1]):
        return num_list.append(int(num_list[-1]) - int(num_list[-2]))
    else:
        return num_list.append(int(num_list[-1] * 2))


print(solution([1, 2, 3, 4]))  # 출력: 1 (4 - 3)
print(solution([4, 3, 2, 1]))  # 출력: 2 (1 * 2)
