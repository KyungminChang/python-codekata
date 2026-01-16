# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 16. 20:57:24

def solution(angle):
    if angle > 0 and angle <90 : 
        return 1
    elif angle == 90 :
        return 2
    elif angle > 90 and angle < 180 :
        return 3
    elif angle == 180 : 
        return 4