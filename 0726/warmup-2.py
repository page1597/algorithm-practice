# 문제: https://codingdojang.com/scode/408
# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. 
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

# 예를들어 S = {1, 3, 4, 8, 13, 17, 20}이 주어졌다면, 
# 결과값은 (3, 4)가 될 것이다.

def shortest(S):
    arr = list(S)  # 이미 정렬된 배열을 리스트로 변환
    min_distance = float('inf')  # 초기값을 무한대로 설정
    min_pair = (None, None)  # 결과 쌍의 초기값

    # 배열을 순회하면서 인접한 두 점 사이의 거리 계산
    for i in range(len(arr) - 1):
        distance = arr[i + 1] - arr[i]
        if distance < min_distance:
            min_distance = distance
            min_pair = (arr[i], arr[i + 1])

    return min_pair


print(shortest({1, 3, 4, 8, 13, 17, 20}))