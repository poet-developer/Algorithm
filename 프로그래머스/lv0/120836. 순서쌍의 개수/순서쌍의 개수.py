def solution(n):
    count = 0 
    m = n
    while m > 0 :
        if n%m == 0 :
            count += 1 
        m -= 1 
    return count