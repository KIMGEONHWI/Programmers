def solution(rsp):
    result = ""
    for move in rsp:
        if move == "2": 
            result += "0"
        elif move == "0":  
            result += "5"
        elif move == "5":  
            result += "2"
    return result
