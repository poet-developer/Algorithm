def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0]>0][dot[1]>0]
# True = 1, False = 0