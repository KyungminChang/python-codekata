# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 22. 10:43:23

def solution(money):
    answer = []
    x = int(money / 5500)
    y = money % 5500 
    answer = [x, y]
    return answer