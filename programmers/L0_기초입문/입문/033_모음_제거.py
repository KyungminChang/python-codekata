# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 02. 02. 10:47:02

def solution(my_string):
    list=["a", "e", "i", "o", "u"]
    for char in list : 
        my_string = my_string.replace(char, "")
    answer = my_string
    return answer