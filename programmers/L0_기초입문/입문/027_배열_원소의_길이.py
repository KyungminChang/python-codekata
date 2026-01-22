# 배열 원소의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 22. 10:40:40

def solution(strlist):
    answer = []
    for i in strlist : 
        answer.append(len(i))
    return answer