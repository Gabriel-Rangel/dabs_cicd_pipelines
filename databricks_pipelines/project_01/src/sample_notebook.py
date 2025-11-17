# Databricks notebook source
# MAGIC %md
# MAGIC # Default notebook
# MAGIC
# MAGIC This default notebook is executed using a Lakeflow job as defined in resources/sample_job.job.yml.

# COMMAND ----------

# Set default catalog and schema
schema = dbutils.widgets.get("schema")
spark.sql(f"USE SCHEMA {schema}")

# COMMAND ----------

print(schema)

# COMMAND ----------

spark.read.table("samples.nyctaxi.trips")