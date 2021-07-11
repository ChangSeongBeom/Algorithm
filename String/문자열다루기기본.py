#https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    slen=len(s)
    answer=False
    if (slen==4 or slen==6) and s.isdigit()==True:
        answer=True
    return answer