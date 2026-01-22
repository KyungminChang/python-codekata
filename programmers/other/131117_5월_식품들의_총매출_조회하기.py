# 5월 식품들의 총매출 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131117
# 작성자: 장경민
# 작성일: 2026. 01. 22. 14:21:27

SELECT
    P.PRODUCT_ID,
    P.PRODUCT_NAME,
    SUM(P.PRICE * O.AMOUNT) AS "총매출" -- 합계를 구함
FROM FOOD_PRODUCT P
JOIN FOOD_ORDER O ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE O.PRODUCE_DATE LIKE '2022-05%'
GROUP BY P.PRODUCT_ID, P.PRODUCT_NAME -- 상품별로 묶음
ORDER BY SUM(P.PRICE * O.AMOUNT) DESC, P.PRODUCT_ID ASC;