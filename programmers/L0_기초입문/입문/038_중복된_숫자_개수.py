# 중복된 숫자 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 02. 05. 14:49:50

def solution(array, n):
    answer = 0
    for i in array :
        if n == i :
            answer += 1
                
    return answer