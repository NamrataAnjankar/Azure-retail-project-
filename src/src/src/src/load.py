from extract import extract_data
from transform import transform_data

def load_data(df):
    df.write \
        .mode("overwrite") \
        .parquet("output/processed_data")

    print("✅ Data Loaded Successfully (Parquet format)")

if __name__ == "__main__":
    df = extract_data()
    df = transform_data(df)
    load_data(df)
