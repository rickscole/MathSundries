
alter procedure micl.math_create_mart as 


-- drop table if exists
if object_id('micl.math_board_size_looping_cum', 'U') is not null
drop table micl.math_board_size_looping_cum; 
if object_id('micl.math_run_count_chi', 'U') is not null
drop table micl.math_run_count_chi; 


-- cumulative percent table
select
    b.board_size
    , cumulative_percent_loop = cast(sum(a.does_congifuration_loop) as decimal(10,4))/ b.board_size
into micl.math_board_size_looping_cum
from micl.math_board_size_looping a 
inner join micl.math_board_size_looping b on a.board_size <= b.board_size
group by 
    b.board_size


-- run counts and chi statistics to test for randomness
;
with t00 as 
(
select
    a.trend_with_magnitude
    , a.does_congifuration_loop
    , trend_magnitude_id = row_number() over(partition by a.does_congifuration_loop order by abs(a.trend_with_magnitude) desc)
    , count = count(*)
from micl.math_board_size_looping_bi a 
where 1 = 1 
    and a.board_size >= 10
group by 
    a.trend_with_magnitude
    , a.does_congifuration_loop
),
t01 as 
(
select 
    run = b.trend_with_magnitude
    , count = max(b.count) - coalesce(max(a.count), 0)
from t00 a 
right join t00 b on 1 = 1
    and a.trend_magnitude_id = b.trend_magnitude_id - 1
    and a.does_congifuration_loop = b.does_congifuration_loop
group by 
    b.trend_with_magnitude
),
t02 as  
(
select 
    a.* 
    , expected_count = cast((b.the_count - abs(a.[run]) + 1) as float) * power(cast(0.5 as float), cast(abs(a.[run]) + 2 as float))
from t01 a 
inner join (select the_count = count(*) from micl.math_board_size_looping_bi where board_size >= 10) b on 1 = 1
)
select
    a.*
    , delta = a.count - a.expected_count
    , chi_squared = power(count - expected_count, 2) / coalesce(expected_count, 0)
into micl.math_run_count_chi
from t02 a
