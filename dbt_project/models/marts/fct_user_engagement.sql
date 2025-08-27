with b as (
  select user_id, sum(session_duration) as total_session_seconds
  from {{ ref('stg_behavioral') }}
  group by user_id
),
g as (
  select
    user_id,
    avg(accuracy) as avg_accuracy,
    avg(reaction_time) as avg_reaction_time,
    sum(levels_completed) as levels_completed_total,
    sum(hints_used) as hints_used_total
  from {{ ref('stg_game_results') }}
  group by user_id
),
o as (
  select
    user_id,
    avg(converted) as conversion_rate,
    avg(churned) as churn_rate
  from {{ ref('stg_operational') }}
  group by user_id
)
select
  d.user_id,
  coalesce(b.total_session_seconds,0) as total_session_seconds,
  coalesce(g.avg_accuracy,0) as avg_accuracy,
  coalesce(g.avg_reaction_time,0) as avg_reaction_time,
  coalesce(g.levels_completed_total,0) as levels_completed_total,
  coalesce(g.hints_used_total,0) as hints_used_total,
  coalesce(o.conversion_rate,0) as conversion_rate,
  coalesce(o.churn_rate,0) as churn_rate
from {{ ref('dim_users') }} d
left join b on d.user_id=b.user_id
left join g on d.user_id=g.user_id
left join o on d.user_id=o.user_id
