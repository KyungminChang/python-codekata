# 오랜 기간 보호한 동물(2)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59411
# 작성자: 장경민
# 작성일: 2026. 01. 19. 10:16:02

-- 코드를 입력하세요
SELECT
AI.ANIMAL_ID
, AI.NAME
FROM ANIMAL_INS AI
JOIN ANIMAL_OUTS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
ORDER BY AO.DATETIME - AI.DATETIME DESC 
LIMIT 2