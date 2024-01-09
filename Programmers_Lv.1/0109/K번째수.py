def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        arrays = array[i - 1 : j]
        arrays.sort()
        re = arrays[k - 1]
        result.append(re)
    return result


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
