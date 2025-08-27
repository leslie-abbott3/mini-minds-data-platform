{% macro date_trunc_grain(grain, ts_col) -%}
    {{ dbt_utils.date_trunc(grain, ts_col) }}
{%- endmacro %}
