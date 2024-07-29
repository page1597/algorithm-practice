from collections import Counter
# 워밍업 문제 6
# 문제: 중복된 숫자 갯수
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120583

# array에 n이 몇 개 있는 지 리턴
def solution(array, n):
    answer = Counter(array)[n]
    return answer

print(solution([1, 1, 2, 3, 4, 5], 1)) # 2