from pyspark.sql.functions import col

def transform_data(df):
    # Remove null values
    df = df.dropna()

    # Convert sales column to integer
    df = df.withColumn("sales", col("sales").cast("int"))

    # Filter records where sales > 100
    df = df.filter(col("sales") > 100)

    print("✅ Data Transformed Successfully")
    df.show()

    return df
