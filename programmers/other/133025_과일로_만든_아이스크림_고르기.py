# 과일로 만든 아이스크림 고르기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133025
# 작성자: 장경민
# 작성일: 2026. 01. 20. 10:42:59

-- 코드를 입력하세요
SELECT
I.FLAVOR
FROM ICECREAM_INFO I
JOIN FIRST_HALF F
ON I.FLAVOR = F.FLAVOR
WHERE F.TOTAL_ORDER > 3000 AND INGREDIENT_TYPE = "fruit_based"