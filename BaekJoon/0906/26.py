def solution(people, limit):
    count = 0
    people.sort()
    start, end = 0, len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        count += 1
    return count


# main
print(solution([70, 80, 50, 50], 100))
# 다 삭제하지 말고 index를 안에 넣어서 index값만 변하게 하기
