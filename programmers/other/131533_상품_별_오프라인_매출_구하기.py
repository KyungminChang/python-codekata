# 상품 별 오프라인 매출 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131533
# 작성자: 장경민
# 작성일: 2026. 01. 19. 10:05:11

-- 코드를 입력하세요
SELECT 
P.PRODUCT_CODE
, SUM(P.PRICE * OS.SALES_AMOUNT) AS SALES
FROM PRODUCT P
JOIN OFFLINE_SALE OS
ON P.PRODUCT_ID = OS.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, P.PRODUCT_CODE ASC