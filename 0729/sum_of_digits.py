# 자릿수 더하기
# 문제: 자릿수 더하기
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 각 자리 숫자의 합
def solution(n):
    # int_arr = map(lambda x: int(x),list(str(n)))
    int_arr = list(map(int, list(str(n))))
    return sum(int_arr)

    # return sum(int(i) for i in str(n))

print(solution(1234))