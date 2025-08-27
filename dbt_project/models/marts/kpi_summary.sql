with f as (select * from {{ ref('fct_user_engagement') }})
select
  count(*) as active_users,
  avg(avg_accuracy) as avg_accuracy,
  avg(conversion_rate) as avg_conversion_rate,
  avg(churn_rate) as avg_churn_rate
from f
