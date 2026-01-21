# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 21. 13:05:41

def solution(slice, n):
    answer = int((n-1) / (slice))+1
    return answer