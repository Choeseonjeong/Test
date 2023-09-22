def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# w,h 중 큰 값은 w에 작은 것은 h에 넣고 각각의 최대값 곱하기 # 와 사람들 천재인 듯
# main
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
