from pyspark.sql import SparkSession  # Ensure correct capitalization

# Create SparkSession
spark = SparkSession.builder \
    .appName("MySparkApp") \
    .getOrCreate()

# Print Spark Session details
print(spark)
spark.stop()

