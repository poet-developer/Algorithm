def solution(numbers):
    sums = 0
    for i in  numbers :
        sums += i
        
    return sums / len(numbers)