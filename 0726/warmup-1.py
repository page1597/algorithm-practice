# 문제: https://codingdojang.com/scode/393
# 1부터 10,000까지 8이라는 숫자가 총 몇 번 나오는가?
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를 들어, 8808은 3, 8888은 4로 카운팅 해야 함) 


# xxx8, xx8x, x8xx, 8xxx
# xxx => 000 ~ 999 : 1000개 x 4 = 4000개

def count_eights():
    count = 0;
    for num in range(1, 10000):
        count += str(num).count('8')
    return count

print(count_eights())