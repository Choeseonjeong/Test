def solution(n, control):
    key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
    return n + sum([key[i] for i in control])


print(solution(0, "wsdawsdassw"))
