# 문자열안에 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 22. 13:45:07

def solution(str1, str2):
    answer = 0
    return 1 if str2 in str1 else 2