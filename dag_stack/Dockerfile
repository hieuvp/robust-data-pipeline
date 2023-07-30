FROM apache/airflow:2.6.3

RUN pip install --upgrade pip && \
    pip install great-expectations && \
    pip install dbt-core dbt-postgres

RUN mkdir -p /home/airflow/.dbt
COPY tmp/profiles.yml /home/airflow/.dbt/profiles.yml
