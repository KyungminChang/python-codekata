# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 21. 13:09:56

def solution(dot):
    answer = 0
    if dot[0] > 0 and dot[1] > 0 :
            answer = 1
    
    elif dot[0] < 0 and dot[1] > 0 :
            answer = 2
    
    elif dot[0] < 0 and dot[1] < 0 :
            answer = 3

    elif dot[0] > 0 and dot[1] < 0 :
            answer = 4
    return answer