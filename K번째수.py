def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_slice = array[commands[i][0] - 1 : commands[i][1]]
        array_slice.sort()
        answer.append(array_slice[commands[i][2]-1])
    return answer