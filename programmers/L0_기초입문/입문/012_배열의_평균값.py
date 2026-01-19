# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 19. 09:44:10

def solution(numbers):
    answer = 0
    sum = 0
    for i in numbers : 
        sum += i 
        answer = sum / len(numbers)
        
    return answer