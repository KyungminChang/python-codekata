# 가격대 별 상품 개수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131530
# 작성자: 장경민
# 작성일: 2026. 01. 20. 10:00:48

-- 코드를 입력하세요
SELECT
    TRUNCATE(PRICE, -4) AS PRICE_GROUP,
    COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP ASC