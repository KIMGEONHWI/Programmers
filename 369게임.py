def solution(order):
    answer = 0
    str_order = str(order)
    for i in str_order :
        if i in ["3", "6", "9"] :
            answer += 1
    return answer