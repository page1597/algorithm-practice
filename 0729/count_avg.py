# 워밍업 문제 4
# 문제: 평균 점수 카운팅 
# 링크: https://100.pyalgo.co.kr/?page=11

def solution(data):
    avg_arr = map(lambda arr: sum(arr) / len(arr), data)
    return len(list(filter(lambda v: v > 80, avg_arr)))

print(solution([[98, 92, 85], [95, 32, 51], [98, 98, 51]]))