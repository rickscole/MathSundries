/*
alter view micl.math_board_size_looping_bi as

select a.* 
, does_congifuration_loop_verbose = case when a.does_congifuration_loop = 1 then 'Yes' else 'No' end
, bin_10 = cast(((a.board_size - 0) - (a.board_size - 0) % 10) as float) / cast(10 as float)
, bin_100 = cast(((a.board_size - 0) - (a.board_size - 0) % 100) as float) / cast(100 as float)
, bin_10_grouping = cast(((a.board_size - 1) - (a.board_size - 1) % 10) as float) / cast(10 as float)
, bin_100_grouping = cast(((a.board_size - 1) - (a.board_size - 1) % 100) as float) / cast(100 as float)
, mod_10 = a.board_size % 10
, mod_100 = a.board_size % 100
, trend_with_magnitude = a.trend * (case when a.does_congifuration_loop = 1 then -1 else 1 end)
from micl.math_board_size_looping a 

select * from micl.math_board_size_looping_bi
*/




select
    b.board_size
    , cumulative_percent_loop = cast(sum(a.does_congifuration_loop) as decimal(10,4))/ b.board_size
-- into micl.math_board_size_looping_cum
from micl.math_board_size_looping a 
inner join micl.math_board_size_looping b on a.board_size <= b.board_size
group by 
    b.board_size



;
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
)
-- /*
select 
    b.trend_with_magnitude as mgt_01
    , a.trend_with_magnitude as mgt_02
    , b.count as count_01
    , a.count as count_02
    -- , max(a.count)
    -- , sum(b.count)
from t00 a 
inner join t00 b on 1 = 1 
    and a.trend_magnitude_id < b.trend_magnitude_id 
    and a.does_congifuration_loop = b.does_congifuration_loop
-- group by 
--    b.trend_with_magnitude
-- */
/*
select
    b.trend_with_magnitude
    , max(b.count) - sum(a.count)
    , max(b.count)
    , sum(a.count)
from t00 a 
inner join t00 b on 1 = 1 
    and a.trend_magnitude_id < b.trend_magnitude_id 
    and a.does_congifuration_loop = b.does_congifuration_loop
group by 
    b.trend_with_magnitude
*/

-- select * from micl.math_board_size_looping_bi



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
)
select 
    run = b.trend_with_magnitude
    , frequency = max(b.count) - coalesce(max(a.count), 0)
from t00 a 
right join t00 b on 1 = 1
    and a.trend_magnitude_id = b.trend_magnitude_id - 1
    and a.does_congifuration_loop = b.does_congifuration_loop
group by 
    b.trend_with_magnitude
