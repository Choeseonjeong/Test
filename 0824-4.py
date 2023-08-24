# A학교에서는 주당 12시간 강의를 기본으로 하고 있다.
# 만약에 강의 시간이 12시간을 초과하면 초과한 시간에 대해 시간당 급여의 30%를 더 지급한다.
# 주당 총 근무 시간과 A학교의 시간당 급여를 입력받아 1주일 급여를 계산하는 프로그램을 작성하시오.

WorkingHours = int(input("근무 시간을 입력하시오. :"))
HourlyRate = int(input("시간당 수당을 입력하시오. :"))

total_Money = WorkingHours * HourlyRate

if WorkingHours > 12:
    additional_money = (WorkingHours - 12) * HourlyRate * 0.3
    total_Money += additional_money

print(total_Money)
