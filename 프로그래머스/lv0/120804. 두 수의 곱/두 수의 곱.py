def solution(num1:int, num2:int) -> int :
    if num1 and num2 < 0 or num1 and num2 >= 100 :
        print("0이상 100이하 수만 입력이 가능합니다.")
        exit
    return num1 * num2