def solution(numbers):
    answer = ''
    data = []
    petch = []
    for i in numbers:
        data.append(str(i))
    petch = sorted(data, key=lambda x: x*3, reverse=True)
    answer = "".join(petch)
    if answer[0] == '0':
        return '0'
    return answer