from pyspark.sql import functions as sf
from pyspark.sql import types as st


def test_spark_range_count(spark):
    assert spark.range(2).count() == 2

def test_group_and_sum(sample_df):
    result = (
        sample_df.groupBy("group")
        .agg(sf.sum("value").alias("total"))
        .where("group = 'A'")
        .first()
    )
    assert isinstance(result, st.Row)
    assert result.total == 30
