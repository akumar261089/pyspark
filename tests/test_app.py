import unittest
from pyspark.sql import SparkSession
from src.utils import process_data

class AppTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.appName("Test").getOrCreate()

    def tearDown(self):
        self.spark.stop()

    def test_process_data(self):
        data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
        df = self.spark.createDataFrame(data, ["Name", "Age"])
        result_df = process_data(df)
        
        expected_data = [("Alice", 34, 68), ("Bob", 45, 90), ("Catherine", 29, 58)]
        expected_df = self.spark.createDataFrame(expected_data, ["Name", "Age", "Age_Doubled"])
        
        self.assertEqual(result_df.collect(), expected_df.collect())

if __name__ == "__main__":
    unittest.main()
