# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 장경민
# 작성일: 2026. 01. 21. 13:22:57

def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                answer += 1  # 제곱근인 경우 (예: 4*4)
            else:
                answer += 2  # 대칭되는 쌍이 있는 경우 (예: 2*8, 8*2)
    return answer