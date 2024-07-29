# 워밍업 문제 5
# 문제: 비트 치환 문제
# 링크: https://100.pyalo.co.kr/?page=30#

def solution(data):
    binary = bin(data)[2:]
    swapped = binary.replace("1", "A").replace("0", "B")
    return swapped

print(solution(5))
