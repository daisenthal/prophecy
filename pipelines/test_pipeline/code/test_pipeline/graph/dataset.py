from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_pipeline.config.ConfigStore import *
from test_pipeline.functions import *

def dataset(spark: SparkSession) -> DataFrame:
    return spark.read.format("iceberg").load("`default`.`david`.`test`")
