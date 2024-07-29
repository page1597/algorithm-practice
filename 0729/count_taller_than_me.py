# 워밍업 문제 7
# 문제: 머쓱이보다 키 큰 사람
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    filtered = filter(lambda x: x > height, array)
    answer = len(list(filtered))
    return answer
print(solution([149, 180, 192, 170], 167))