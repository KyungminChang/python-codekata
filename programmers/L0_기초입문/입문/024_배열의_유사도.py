# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 21. 13:14:19

def solution(s1, s2):
    answer = 0
    for i in s1 :
        for j in s2 :
            if i == j :
                answer += 1
    return answer