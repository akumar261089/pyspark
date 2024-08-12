from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def process_data(df: DataFrame) -> DataFrame:
    return df.withColumn("Age_Doubled", col("Age") * 2)
