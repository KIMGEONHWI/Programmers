def solution(money):
    count = money // 5500
    return [count, money - count * 5500 ]