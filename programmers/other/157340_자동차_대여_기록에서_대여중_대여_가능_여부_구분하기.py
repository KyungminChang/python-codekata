# 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157340
# 작성자: 장경민
# 작성일: 2026. 02. 05. 14:59:45

-- 코드를 입력하세요
SELECT 
    DISTINCT CAR_ID,
    CASE 
        WHEN CAR_ID IN (
            SELECT CAR_ID 
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
            WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE
        ) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC;