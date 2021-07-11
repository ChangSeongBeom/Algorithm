#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    result = []
    for i in range(0, len(commands)):
        first = commands[i][0]
        second = commands[i][1]
        target = commands[i][2]

        tmp = sorted(array[first - 1:second])
        result.append(tmp[target - 1])
    return result

