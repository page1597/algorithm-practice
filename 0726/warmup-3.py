import re
# 문제: https://100.jsalgo.co.kr/?page=4#
# 첫번째 시도에서 나온 값은 곱하기 1을 하고, 
# 두번째 시도에서 나온 값은 곱하기 2를 하고,
# 세번째 시도에서 나온 값은 곱하기 3을 하기로 하였습니다. 
# 라이캣이 가져갈 쿠키의 수를 리턴하는 함수를 완성해주세요
# ['쿠키 3개', '쿠키 2개', '쿠키 5개'] -> 22
# (3 * 1) + (2 * 2) + (5 * 3) = 22 
def solution(cookies):
    answer = 0;
    for i, s in enumerate(cookies):
        numbers = re.findall(r'\d+', s)
        answer += int(numbers[0]) * (i+1)
    return answer;
        
print(solution(['쿠키 3개', '쿠키 2개', '쿠키 5개']))