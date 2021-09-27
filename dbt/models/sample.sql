{{ config(materialized='table') }}

with stations as (

    select *
        
        -- {% for col in ['flow_99','flow_max','flow_median','flow_total','n_obs'] %}
        --     case
        --         when isnull({{col}}) then 0 else {{col}}
        --     end as {{col}}
        --     {% if not loop.last %},{% endif %}
        -- {% endfor %}
    from foo.station_summary

)

select *
from stations