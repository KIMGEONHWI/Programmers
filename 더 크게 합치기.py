def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    if ab > ba :
        return ab
    elif ab < ba :
        return ba
    else :
        return ab
    
