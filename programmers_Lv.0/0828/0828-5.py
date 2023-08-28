# 나이 출력

# 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다.
# 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.


def solution(age):
    return 2022 - int(age) + 1


# main

# age = map(int, input().split()) # map함수가 리스트, 튜플 등에 값을 저장하는 것이므로
age = input("나이를 입력하세요: ")  # 하나가 필요할 때는 이렇게 함
k = solution(age)
print(k)
