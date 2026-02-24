# 주문량이 많은 아이스크림들 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133027
# 작성자: 장경민
# 작성일: 2026. 02. 24. 17:48:51

with J as (SELECT
FLAVOR
, sum(TOTAL_ORDER) as TOTAL
FROM JULY
GROUP BY FLAVOR
ORDER BY TOTAL DESC)
SELECT 
    F.FLAVOR
FROM FIRST_HALF F
JOIN J ON F.FLAVOR = J.FLAVOR
ORDER BY 
    (F.TOTAL_ORDER + J.TOTAL) DESC
limit 3
