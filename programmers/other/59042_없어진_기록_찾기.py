# 없어진 기록 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59042
# 작성자: 장경민
# 작성일: 2026. 01. 22. 14:41:01

-- 코드를 입력하세요
SELECT
O.ANIMAL_ID
, O.NAME
FROM ANIMAL_OUTS O
LEFT JOIN  ANIMAL_INS I
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME IS NULL
ORDER BY O.ANIMAL_ID