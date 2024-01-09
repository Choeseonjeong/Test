def solution(rsp):
    a = {2: 0, 0: 5, 5: 2}
    result = []
    for i in rsp:
        result.append(str(a[int(i)]))
    return "".join(result)


print(solution("205"))
