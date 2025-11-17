import argparse
from databricks.sdk.runtime import spark
from project_02 import taxis


def main():
    # Process command-line arguments
    parser = argparse.ArgumentParser(description="Databricks job with schema parameter")
    parser.add_argument("--schema", required=True)
    args = parser.parse_args()

    # Set the default catalog and schema)
    spark.sql(f"USE SCHEMA {args.schema}")

    # Example: just find all taxis from a sample catalog
    taxis.find_all_taxis().show(5)


if __name__ == "__main__":
    main()
