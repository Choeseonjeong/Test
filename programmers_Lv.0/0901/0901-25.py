# 최댓값 만들기 (2)
# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.


def solution(numbers):
    numbers.sort()
    return (
        int(numbers[-1]) * int(numbers[-2])
        if int(numbers[-1]) * int(numbers[-2]) > int(numbers[0]) * int(numbers[1])
        else int(numbers[0]) * int(numbers[1])
    )


def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1], numbers[-2])


# main
numbers = list(input().split(","))
print(solution(numbers))
