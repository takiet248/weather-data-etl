from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

jdbc_driver_path = "/Users/tim301248/Desktop/Data Engineer/weather/jars/postgresql-42.6.0.jar"

# Initialize Spark session
spark = SparkSession.builder \
    .appName("WeatherETL") \
    .config("spark.jars", jdbc_driver_path) \
    .getOrCreate()
    
# Load raw data
df = spark.read.csv("/Users/tim301248/Desktop/Data Engineer/weather/data/weather.csv", header=True, inferSchema=True)

# Convert temperature to Celsius
df_transformed = df.withColumn("temperature_c", col("temperature"))

# Compute average daily temperature per location
df_avg_temp = df_transformed.groupBy("date", "location").agg(avg("temperature_c").alias("avg_temp"))

df_avg_temp.show(5)
# Write to PostgreSQL
db_url = "jdbc:postgresql://localhost:5432/weather_db"
properties = {"user": "airflow", "password": "airflow", "driver": "org.postgresql.Driver"}

df_avg_temp.write.jdbc(url=db_url, table="weather_data", mode="overwrite", properties=properties)

spark.stop()
