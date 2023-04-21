def solution(rsp):
    answer = ''
    list1 = list(rsp)
    for i in list1 :
        if int(i)  == 0 :
            i = 5
            answer += str(i)
        elif int(i)  == 2 :
            i = 0
            answer += str(i)
        else :
            i = 2
            answer += str(i)
    return answer
    
    # return answer