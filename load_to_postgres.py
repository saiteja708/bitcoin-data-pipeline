import psycopg2
import pandas as pd

print("✅ Step 3: Loading data to PostgreSQL...")

# Load CSV
df = pd.read_csv("bitcoin.csv")

# Connect to DB
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="teja@1819",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Insert data
rows_inserted = 0

for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO bitcoin_prices (date, price) VALUES (%s, %s)",
        (row['date'], float(row['price']))
    )
    rows_inserted += 1

conn.commit()
cursor.close()
conn.close()

print(f"✅ Data loaded successfully! Rows inserted: {rows_inserted}")
