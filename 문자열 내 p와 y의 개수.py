def solution(s):
    answer = True
    low = s.lower()
    if low.count("p") == low.count("y"):
        return True
    else: 
        return False
    return True