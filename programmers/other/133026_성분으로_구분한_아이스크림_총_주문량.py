# 성분으로 구분한 아이스크림 총 주문량
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133026
# 작성자: 장경민
# 작성일: 2026. 01. 19. 10:30:48

-- 코드를 입력하세요
SELECT
I.INGREDIENT_TYPE
, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF F
JOIN ICECREAM_INFO I
ON F.FLAVOR = I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC