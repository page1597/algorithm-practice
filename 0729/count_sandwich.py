from collections import deque

# 스택 | 큐
# 샌드위치 포장 문제
def solution(data):
    stack = []
    sandwich_count = 0
    pattern = [1, 2, 3, 4, 1]

    for item in data:
        stack.append(item)
        if stack[-len(pattern):] == pattern:
            stack = stack[:-len(pattern)]
            sandwich_count += 1

    return sandwich_count
