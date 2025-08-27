with src as (
  select
    user_id,
    date,
    converted::integer as converted,
    churned::integer as churned,
    plan_tier
  from operational
)
select * from src
