# 조건에 맞는 사용자 정보 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164670
# 작성자: 장경민
# 작성일: 2026. 01. 22. 15:09:08

-- 코드를 입력하세요
SELECT
U.USER_ID
, U.NICKNAME
, CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) AS "전체주소"
, CONCAT(LEFT(U.TLNO, 3), '-', SUBSTR(U.TLNO, 4, 4), '-', RIGHT(U.TLNO, 4)) AS "전화번호"
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
GROUP BY U.USER_ID, U.NICKNAME, U.CITY, U.STREET_ADDRESS1, U.STREET_ADDRESS2, U.TLNO
HAVING COUNT(B.BOARD_ID) >=3
ORDER BY U.USER_ID DESC