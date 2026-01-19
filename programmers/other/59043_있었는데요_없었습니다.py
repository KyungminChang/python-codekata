# 있었는데요 없었습니다
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59043
# 작성자: 장경민
# 작성일: 2026. 01. 19. 10:10:11

-- 코드를 입력하세요
SELECT 
AI.ANIMAL_ID
, AI.NAME
FROM ANIMAL_INS AI
JOIN ANIMAL_OUTS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AI.DATETIME > AO.DATETIME
ORDER BY AI.DATETIME ASC