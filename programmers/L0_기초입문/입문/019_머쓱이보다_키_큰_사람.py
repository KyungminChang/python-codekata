# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 20. 09:25:36

def solution(array, height):
    count = 0
    answer = 0
    for i in array :
        if i > height : 
            count += 1
    answer = count
    return answer