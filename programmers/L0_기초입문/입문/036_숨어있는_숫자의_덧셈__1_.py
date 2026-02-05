# 숨어있는 숫자의 덧셈 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 02. 05. 14:41:10

def solution(my_string):
    answer = 0
    sum = 0
    s = my_string[::1]
    for i in s :
        if i.isdigit() :
            sum += int(i)
    
    answer = sum
        
    return answer