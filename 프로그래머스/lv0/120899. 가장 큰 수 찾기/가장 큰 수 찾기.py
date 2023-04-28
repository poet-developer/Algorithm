def solution(array):
    list1 = sorted(array)
    answer = [list1[-1],array.index(list1[-1])]
    return answer