# 숨어있는 숫자의 덧셈 (1)
# 문자열 my_string이 매개변수로 주어집니다.
# my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.


def solution(my_string):
    sum = 0
    for i in my_string:
        if i.isdigit():
            sum += int(i)
    return sum


# main
my_string = input()
print(solution(my_string))

# isdigit()가 숫자,문자 판별함
