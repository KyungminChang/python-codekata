# 년, 월, 성별 별 상품 구매 회원 수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131532
# 작성자: 장경민
# 작성일: 2026. 02. 05. 20:12:37

-- 코드를 입력하세요
SELECT 
    YEAR(O.SALES_DATE) AS YEAR, 
    MONTH(O.SALES_DATE) AS MONTH, 
    U.GENDER, 
    COUNT(DISTINCT U.USER_ID) AS USERS 
FROM USER_INFO U
JOIN ONLINE_SALE O ON U.USER_ID = O.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;