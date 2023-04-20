def solution(emergency):
    answer = []
    list1 = sorted(emergency, reverse = True); 
    # 순서정렬
    for i in emergency : 
        answer.append(list1.index(i)+1)
    return answer
        