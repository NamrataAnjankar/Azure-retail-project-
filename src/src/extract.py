from spark_session import create_spark_session

def extract_data():
    spark = create_spark_session()

    df = spark.read \
        .option("header", True) \
        .csv("data/sample_data.csv")

    print("✅ Data Extracted Successfully")
    df.show()

    return df

if __name__ == "__main__":
    extract_data()
