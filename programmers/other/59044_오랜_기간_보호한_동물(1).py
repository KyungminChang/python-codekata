# 오랜 기간 보호한 동물(1)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59044
# 작성자: 장경민
# 작성일: 2026. 01. 21. 13:52:22

-- 코드를 입력하세요
SELECT
AI.NAME
, AI.DATETIME
FROM ANIMAL_INS AI
LEFT JOIN ANIMAL_OUTS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AO.ANIMAL_ID IS NULL 
ORDER BY AI.DATETIME ASC LIMIT 3