# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 02. 05. 09:31:35

def solution(num_list):
    hol = 0
    zzack = 0
    for i in num_list :
        if i % 2 == 0 : 
            zzack += 1
            
        else : 
            hol +=1
            
    answer = [zzack, hol]
    return answer