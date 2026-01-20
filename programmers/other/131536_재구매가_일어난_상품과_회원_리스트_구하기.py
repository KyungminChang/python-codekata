# 재구매가 일어난 상품과 회원 리스트 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131536
# 작성자: 장경민
# 작성일: 2026. 01. 20. 10:43:31

-- 코드를 입력하세요
SELECT
USER_ID,
PRODUCT_ID
FROM ONLINE_SALE
group by USER_ID, PRODUCT_ID
having count(*) > 1
ORDER BY USER_ID asc, PRODUCT_ID desc