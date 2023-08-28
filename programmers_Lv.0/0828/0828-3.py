# 숫자 비교하기
# 정수 num1과 num2가 매개변수로 주어집니다.
# 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.


def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1


# 원한 것
def solution(num1, num2):
    return 1 if num1 == num2 else -1
    # return (true일 때 반환할 것) (조건문)


# main

num1, num2 = map(int, input().split())
k = solution(num1, num2)
print(k)
