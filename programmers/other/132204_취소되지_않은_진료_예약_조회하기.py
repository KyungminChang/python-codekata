# 취소되지 않은 진료 예약 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132204
# 작성자: 장경민
# 작성일: 2026. 01. 22. 15:45:09

SELECT 
    A.APNT_NO, 
    P.PT_NAME, 
    P.PT_NO, 
    A.MCDP_CD, 
    D.DR_NAME, 
    A.APNT_YMD
FROM APPOINTMENT A
JOIN PATIENT P ON A.PT_NO = P.PT_NO
JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE A.MCDP_CD = 'CS' 
  AND A.APNT_CNCL_YN = 'N'
  AND A.APNT_YMD LIKE '2022-04-13%'
ORDER BY A.APNT_YMD ASC