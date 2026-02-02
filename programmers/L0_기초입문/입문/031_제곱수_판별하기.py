# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 02. 02. 10:29:34

def solution(n):
    answer = 0
    i=1
    while i**2 <= n :
        if i**2 == n  :
            answer = 1
            return answer
        else : i+=1
    
    answer = 2
    return answer