# 올바른 괄호


def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack):
            stack.pop()
        else:
            return False
    return False if len(stack) else True


print(solution("(()("))
