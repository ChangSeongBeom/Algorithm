#https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    result = []
    phonelen = len(phone_number)
    for phone_num in range(0, len(phone_number)):
        if phone_num <= phonelen - 5:
            result.append('*')
        else:
            result.append(phone_number[phone_num])
    return (''.join(result))
