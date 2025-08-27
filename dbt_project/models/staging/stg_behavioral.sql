with src as (
  select
    user_id,
    session_id,
    session_start,
    session_end,
    session_duration::integer as session_duration
  from behavioral
)
select * from src
