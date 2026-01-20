# 대여 기록이 존재하는 자동차 리스트 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157341
# 작성자: 장경민
# 작성일: 2026. 01. 20. 10:05:10

-- 코드를 입력하세요
SELECT
DISTINCT(C.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
ON C.CAR_ID = CH.CAR_ID
WHERE C.CAR_TYPE = "세단" AND CH.START_DATE LIKE ("2022-10%")
ORDER BY C.CAR_ID DESC
