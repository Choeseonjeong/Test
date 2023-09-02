# 배열 두배 만들기
# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 각 원소에 두배한 원소를 가진 배열 return


# def solution(numbers):
#     answer = []
#     for i in numbers:
#         answer.append(int(i) * 2)
#     return answer


def solution(numbers):
    return [n * 2 for n in numbers]


# main
numbers = list(input().split(","))
print(solution(numbers))
