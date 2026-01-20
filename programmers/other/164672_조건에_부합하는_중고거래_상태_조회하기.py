# 조건에 부합하는 중고거래 상태 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164672
# 작성자: 장경민
# 작성일: 2026. 01. 20. 10:49:37

-- 코드를 입력하세요
SELECT
BOARD_ID
,WRITER_ID
,TITLE
,PRICE
,CASE 
        WHEN STATUS = 'SALE' THEN '판매중'
        WHEN STATUS = 'RESERVED' THEN '예약중'
        WHEN STATUS = 'DONE' THEN '거래완료'
    END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE  LIKE ("2022-10-05%")
ORDER BY BOARD_ID DESC