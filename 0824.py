# -*- coding: utf-8 -*-


# 세 과목(국어, 수학, 영어) 성적을 input()함수로 입력받아 세 과목의 총점과 평균을
# 구하는 프로그램을 작성하시오. 평균은 소수점 둘째 자리까지 출력되도록 한다.

x1 = int(input('enter your korean score : ' ))
x2 = int(input('enter your math score : ' ))
x3 = int(input('enter your english score : ' ))

print(' input score ')
print('-----------')

print('korean score' , x1)
print('math score' , x2)
print('english score' , x3)

sum = x1+x2+x3
avg = sum/3
avg = round(avg,2)


print('total score :',sum)
print('avg score : ',avg)

