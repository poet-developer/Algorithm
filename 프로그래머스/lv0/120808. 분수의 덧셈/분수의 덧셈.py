def solution(numer1, denom1, numer2, denom2):
    y = denom1 * denom2
    x1 = numer1*denom2
    x2 = numer2*denom1
    x3 = x1+x2
    count = 1
    same = [1]
    answer = []
    
    if(x3 >= y) :
        j = y
    else :
        j = x3
    
    for i in range(1,j+1) :
        if x3%count == 0 and y%count == 0 :
            same.append(count)
        count = count + 1
    answer.append(x3/max(same))
    answer.append(y/max(same))

    return answer
