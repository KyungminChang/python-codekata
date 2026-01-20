# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 20. 09:09:37

def solution(n, t):
    answer = n
    for n in range(t) :
        answer *= 2
    return answer