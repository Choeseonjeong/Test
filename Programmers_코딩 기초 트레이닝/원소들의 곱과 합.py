def solution(num_list):
    a = 1
    for i in num_list:
        a = a * i
        b = sum(i for i in num_list)
    return 0 if a > b * b else 1


print(solution([3, 4, 5, 2, 1]))
