import os

import pytest

if not str(os.getenv("SPARK_VERSION")).startswith("4.0"):
    pytest.skip(
        "Skipping tests because Spark version is not compatible",
        allow_module_level=True,
    )

def test_spark_ansi_mode(spark):
    assert spark.conf.get("spark.sql.ansi.enabled") == "true"
