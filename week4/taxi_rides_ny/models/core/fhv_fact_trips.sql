{{
    config(
        materialized='table'
    )
}}


with fhv_tripdata as (
    select *
    from {{ ref('stg_staging__fhv_tripdata2019') }}
),
dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)

SELECT 
    fhv_tripdata.*,
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone as pickup_zone,
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone as dropoff_zone
FROM fhv_tripdata
inner join dim_zones as pickup_zone
on fhv_tripdata.pulocationid = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on fhv_tripdata.dolocationid = dropoff_zone.locationid