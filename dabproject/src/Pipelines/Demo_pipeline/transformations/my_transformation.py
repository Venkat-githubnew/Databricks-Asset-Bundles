from pyspark import pipelines as dp

@dp.materialized_view()
def demo_data():
    """Demo materialized view with 10 rows (id: 0-9)"""
    return spark.range(10)
