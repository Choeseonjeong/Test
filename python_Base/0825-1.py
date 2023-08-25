# for 구문과 range() 함수를 이용하여 다음과 같이 출력되도록 하시오.
# 0 1 2 3 4 5 6 7 8 9
# 0 5 10 15 20 25 35 40 45 50
# 10 9 8 7 6 5 4 3 2 1


for i in range(10):
    print(i, end=" ")

print()

for i in range(0, 51, 5):
    print(i, end=" ")

print()

for i in range(10, 0, -1):
    print(i, end=" ")
