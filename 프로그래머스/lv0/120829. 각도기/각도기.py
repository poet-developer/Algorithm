def solution(angle):
    answer = 4
    if 0 < angle and angle < 90 :
        return 1
    elif 90 == angle : 
        return 2
    elif 90 < angle and angle < 180 :
        return 3
    else :
        return answer