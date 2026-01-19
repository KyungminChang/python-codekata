# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 19. 09:31:46

def solution(n, k):
    x = n * 12000
    y = k * 2000  - int(n/10) * 2000
    answer = x + y
    return answer