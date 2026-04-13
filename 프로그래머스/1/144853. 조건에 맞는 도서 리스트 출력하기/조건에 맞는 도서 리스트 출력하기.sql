-- 코드를 입력하세요
SELECT book_id, to_char(published_date, 'YYYY-MM-DD') as publisehd_date from book where to_char(published_date, 'YYYY') like '2021' and category like '인문' order by published_date asc;

