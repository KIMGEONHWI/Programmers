def solution(num_list):
    even = ""
    add = ""
    for i in num_list:
        if i % 2 == 0 :
            even += str(i)
        elif i % 2 == 1 :
            add += str(i)
    return int(even) + int(add)