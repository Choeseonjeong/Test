# 부족한 금액 계산하기


def solution(price, money, count):
    result = 0
    price_result = 0
    for i in range(count):
        price_result += price
        result += price_result
    return result - money if result > money else 0


print(solution(3, 20, 4))
