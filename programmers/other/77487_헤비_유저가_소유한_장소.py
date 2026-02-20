# 헤비 유저가 소유한 장소
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77487
# 작성자: 장경민
# 작성일: 2026. 02. 20. 17:37:48

SELECT
*
FROM PLACES
WHERE HOST_ID IN (
SELECT
HOST_ID
FROM PLACES
GROUP BY HOST_ID
HAVING COUNT(HOST_ID) >= 2
)
ORDER BY ID ASC