#https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    tmp=[]
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            tmp.append(numbers[i]+numbers[j])
    result=sorted(list(set(tmp)))
    return (result)