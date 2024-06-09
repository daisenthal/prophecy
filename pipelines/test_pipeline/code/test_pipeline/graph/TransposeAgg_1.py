from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_pipeline.config.ConfigStore import *
from test_pipeline.functions import *

def TransposeAgg_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.agg()
