# 서울에 위치한 식당 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131118
# 작성자: 장경민
# 작성일: 2026. 02. 19. 17:56:27

-- 코드를 입력하세요
SELECT 
ri.REST_ID
, ri.REST_NAME
, ri.FOOD_TYPE
, ri.FAVORITES
, ri.ADDRESS
, ROUND(AVG(rr.REVIEW_SCORE), 2) as SCORE_AVG
FROM REST_INFO as ri
INNER JOIN REST_REVIEW as rr
ON ri.REST_ID = rr.REST_ID
WHERE ri.ADDRESS like "서울%"
GROUP BY ri.REST_ID
, ri.REST_NAME
, ri.FOOD_TYPE
, ri.FAVORITES
, ri.ADDRESS
ORDER BY SCORE_AVG DESC, ri.FAVORITES desc