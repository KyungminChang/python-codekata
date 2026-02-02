# 특정 문자 제거하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 02. 02. 10:36:23

def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    
    return answer