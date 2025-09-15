import os

import pytest

if not str(os.getenv("SPARK_VERSION")).startswith("3.5"):
    pytest.skip(
        "Skipping tests because Spark version is not compatible",
        allow_module_level=True,
    )

@pytest.mark.skipif(False, reason="Skip for non-Spark 3.5")
def test_spark_ansi_mode(spark):
    assert spark.conf.get("spark.sql.ansi.enabled") == "false"
