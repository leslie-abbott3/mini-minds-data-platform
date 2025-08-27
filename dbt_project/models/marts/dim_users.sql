with users as (
  select distinct user_id
  from {{ ref('stg_behavioral') }}
  union
  select distinct user_id from {{ ref('stg_operational') }}
  union
  select distinct user_id from {{ ref('stg_game_results') }}
)
select
  user_id
from users
