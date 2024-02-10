```
CREATE OR REPLACE EXTERNAL TABLE intrepid-axe-411322.ny_taxi.external_green_tripdata
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://zoomcamp-week3-george-zakhem/green_taxi_2022.parquet']
);

CREATE OR REPLACE TABLE intrepid-axe-411322.ny_taxi.green_tripdata_non_partitioned AS
SELECT * FROM intrepid-axe-411322.ny_taxi.external_green_tripdata;

SELECT lpep_pickup_datetime from `ny_taxi.external_green_tripdata`;
 
SELECT Date(TIMESTAMP_MICROS(CAST(1640996061000000000 / 1000 AS INT64))) AS timestamp_value;

SELECT COUNT(*) FROM `ny_taxi.external_green_tripdata`;

SELECT DISTINCT(PULocationID) FROM `ny_taxi.external_green_tripdata`;

SELECT DISTINCT(PULocationID) FROM `ny_taxi.green_tripdata_non_partitioned`;

SELECT count(*) FROM `ny_taxi.external_green_tripdata`
where fare_amount=0;

SELECT count(*) FROM `ny_taxi.green_tripdata_non_partitioned`
where fare_amount = 0;

SELECT DISTINCT(PULocationID) from `ny_taxi.green_tripdata_non_partitioned`
where DATE(TIMESTAMP_MICROS(CAST(lpep_pickup_datetime /1000 AS INT64))) BETWEEN '2022-06-01' AND '2022-07-01';

ALTER TABLE `intrepid-axe-411322.ny_taxi.green_tripdata_non_partitioned`
ADD COLUMN lpep_pickup_date DATE;

UPDATE `intrepid-axe-411322.ny_taxi.green_tripdata_non_partitioned`
SET lpep_pickup_date = DATE(TIMESTAMP_MICROS(CAST(lpep_pickup_datetime /1000 AS INT64)))
WHERE 1=1;

CREATE OR REPLACE TABLE intrepid-axe-411322.ny_taxi.green_tripdata_partitioned
PARTITION BY
lpep_pickup_date
CLUSTER BY PULocationID AS
SELECT * FROM `intrepid-axe-411322.ny_taxi.green_tripdata_non_partitioned`;


SELECT DISTINCT(PULocationID) from `ny_taxi.green_tripdata_partitioned`
where lpep_pickup_date BETWEEN '2022-06-01' AND '2022-07-01';
```
