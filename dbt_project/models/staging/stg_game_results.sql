with src as (
  select
    user_id,
    game_id,
    timestamp,
    cast(reaction_time as float) as reaction_time,
    cast(accuracy as float) as accuracy,
    cast(levels_completed as integer) as levels_completed,
    cast(hints_used as integer) as hints_used,
    cast(has_learning_disability as integer) as has_learning_disability
  from game_results
)
select * from src
