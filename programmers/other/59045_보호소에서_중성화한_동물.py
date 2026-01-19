# 보호소에서 중성화한 동물
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59045
# 작성자: 장경민
# 작성일: 2026. 01. 19. 10:20:39

-- 코드를 입력하세요
SELECT
AI.ANIMAL_ID
, AI.ANIMAL_TYPE
, AI.NAME
FROM ANIMAL_INS AI
JOIN ANIMAL_OUTS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AI.SEX_UPON_INTAKE like 'intact%' 
and(AO.SEX_UPON_OUTCOME LIKE 'Spayed%' OR AO.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY AI.ANIMAL_ID