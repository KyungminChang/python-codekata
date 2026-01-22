# 식품분류별 가장 비싼 식품의 정보 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131116
# 작성자: 장경민
# 작성일: 2026. 01. 22. 13:53:34

-- 코드를 입력하세요
SELECT 
CATEGORY
, PRICE
, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN 
(
SELECT CATEGORY, MAX(PRICE)
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
GROUP BY CATEGORY
 )
ORDER BY PRICE DESC