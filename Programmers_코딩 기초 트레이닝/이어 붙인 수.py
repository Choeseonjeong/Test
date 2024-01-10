def solution(num_list):
    a = ""
    b = ""
    for i in num_list:
        if i % 2 == 0:
            a = a + str(i)
        else:
            b = b + str(i)
    a = "".join(a)
    b = "".join(b)
    return int(a) + int(b)


print(solution([3, 4, 5, 2, 1]))
