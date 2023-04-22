import re

def solution(my_string):
    string = re.sub(r'[^0-9]', '', my_string)
    answer = []
    for i in string :
        answer.append(int(i))
    answer.sort()
    
    return answer