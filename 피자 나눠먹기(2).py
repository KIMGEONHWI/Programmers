def solution(n):
    for i in range(1, 6*n+1):
        if i % 6 == 0 and i % n == 0:
            return i // 6
