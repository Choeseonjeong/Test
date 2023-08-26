# flag에 따라 다른 값 반환하기

# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때,
# flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.


def solution(a, b, flag):
    if flag:
        return a + b
    return a - b


# flag 자체가 true,false기 때문에 if flag가 true일떄로 가능
