# 옷가게 할인 받기

# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%,
# 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.


def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000 and price < 500000:
        return int(price * 0.9)
    elif price >= 100000 and price < 300000:
        return int(price * 0.95)
    else:
        return int(price)


# main
price = int(input())
print(solution(price))


# 두 개의 값이 연결되어 있으면 딕셔너리 사용
def solution(price):
    price_sale = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, price_sale in price_sale.items():
        if price >= discount_price:
            return int(price * price_sale)
