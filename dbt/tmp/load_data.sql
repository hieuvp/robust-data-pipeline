CREATE TABLE taxi_zone_lookup
(
    locationid   INTEGER NOT NULL,
    borough      VARCHAR NOT NULL,
    zone         VARCHAR,
    service_zone VARCHAR
);

COPY taxi_zone_lookup
    FROM '/tmp/taxi_zone_lookup.csv'
    DELIMITER ',' CSV HEADER;

ALTER TABLE taxi_zone_lookup
    OWNER TO demo_user;

CREATE TABLE yellow_tripdata_sample_2019_01
(
    vendor_id           INTEGER NOT NULL,
    pickup_datetime     TIMESTAMP WITHOUT TIME ZONE,
    dropoff_datetime    TIMESTAMP WITHOUT TIME ZONE,
    passenger_count     INTEGER NOT NULL,
    pickup_location_id  DECIMAL NOT NULL,
    dropoff_location_id DECIMAL NOT NULL,
    fare_amount         DECIMAL NOT NULL
);

COPY yellow_tripdata_sample_2019_01
    FROM '/tmp/yellow_tripdata_sample_2019_01.csv'
    DELIMITER ',' CSV HEADER;

ALTER TABLE yellow_tripdata_sample_2019_01
    OWNER TO demo_user;

CREATE TABLE yellow_tripdata_sample_2019_02
(
    vendor_id           INTEGER NOT NULL,
    pickup_datetime     TIMESTAMP WITHOUT TIME ZONE,
    dropoff_datetime    TIMESTAMP WITHOUT TIME ZONE,
    passenger_count     INTEGER NOT NULL,
    pickup_location_id  DECIMAL NOT NULL,
    dropoff_location_id DECIMAL NOT NULL,
    fare_amount         DECIMAL NOT NULL
);

COPY yellow_tripdata_sample_2019_02
    FROM '/tmp/yellow_tripdata_sample_2019_02.csv'
    DELIMITER ',' CSV HEADER;

ALTER TABLE yellow_tripdata_sample_2019_02
    OWNER TO demo_user;
