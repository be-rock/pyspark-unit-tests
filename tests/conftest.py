import pytest

from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    spark_session = (
        SparkSession.builder
        .master("local[*]")
        .appName("pytest-pyspark-testing")
        .getOrCreate()
    )
    yield spark_session
    spark_session.stop()

@pytest.fixture
def sample_df(spark):
    data = [("A", 10), ("A", 20), ("B", 5)]
    return spark.createDataFrame(data, ["group", "value"])
