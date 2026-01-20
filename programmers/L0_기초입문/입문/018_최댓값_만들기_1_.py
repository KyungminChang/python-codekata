# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 20. 09:18:48

def solution(numbers):
    numbers.sort()
    x= numbers[-1]
    y= numbers[-2]
    answer = x * y
    return answer