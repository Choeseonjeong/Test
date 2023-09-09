# commans 자체가 2차원 배열
# i,j,k
# i 부터 j까지 자르고 정렬한 후 k번째 숫자


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        slice_array = array[i - 1 : j]
        sort_slice_array = sorted(slice_array)
        answer.append(sort_slice_array[k - 1])
    return answer


# main
array = list(map(int, input().split(",")))
commands = []
for i in range(3):
    a = list(map(int, input().split(",")))
    commands.append(a)

print(solution(array, commands))
