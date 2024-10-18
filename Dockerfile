FROM marcorezende/spark-delta-aws:3.5.0
USER root
RUN pip install pandas duckdb