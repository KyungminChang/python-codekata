# 조건에 맞는 사용자와 총 거래금액 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164668
# 작성자: 장경민
# 작성일: 2026. 01. 21. 14:41:24

-- 코드를 입력하세요
SELECT
U.USER_ID
, U.NICKNAME
, SUM(PRICE) AS "총거래금액"
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
WHERE STATUS = "DONE" 
GROUP BY U.USER_ID, U.NICKNAME 
HAVING SUM(PRICE)>=700000 
ORDER BY SUM(PRICE) ASC 