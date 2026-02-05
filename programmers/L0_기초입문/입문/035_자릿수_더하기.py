# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 02. 05. 09:45:22

def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10
    return answer