def solution(num_list, n):
    a = []
    for i in range(0, len(num_list), n):
        a.append(num_list[i])
    return a


print(solution([4, 2, 6, 1, 7, 6], 2))
