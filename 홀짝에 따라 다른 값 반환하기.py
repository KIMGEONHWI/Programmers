def solution(n):
    sum1 = 0
    sum2 = 0
    if (n % 2 == 0) :
        for i in range(1, n+1) :
            if (i % 2 == 0) :
                sum1 += i ** 2
        return sum1
    else :
        for j in range(1, n+1) :
            if j % 2 == 1:
                sum2 += j
        return sum2