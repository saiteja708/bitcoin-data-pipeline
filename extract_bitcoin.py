import requests
import pandas as pd

print("✅ Step 1: Extracting Bitcoin data...")

# API call
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {"vs_currency": "usd", "days": 1}

response = requests.get(url, params=params)
data = response.json()

# Convert to dataframe
df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])

# Convert timestamp to date
df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
df = df[['date', 'price']]

# Save file
df.to_csv("bitcoin.csv", index=False)

print("✅ bitcoin.csv created successfully!")