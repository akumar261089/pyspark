from pyspark.sql import SparkSession
from src.utils import process_data

def main():
    spark = SparkSession.builder.appName("SamplePySparkApp").getOrCreate()
    
    data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
    df = spark.createDataFrame(data, ["Name", "Age"])
    
    processed_df = process_data(df)
    processed_df.show()

if __name__ == "__main__":
    main()
