import pandas as pd
import matplotlib.pyplot as plt

print("✅ Step 2: Creating charts...")

df = pd.read_csv("bitcoin.csv")
df['date'] = pd.to_datetime(df['date'])

# 1. Line chart
plt.figure()
plt.plot(df['date'], df['price'])
plt.title("Bitcoin Price Trend")
plt.xticks(rotation=45)
plt.savefig("price_trend.png")
plt.close()

# 2. Histogram
plt.figure()
df['price'].hist()
plt.title("Price Distribution")
plt.savefig("price_distribution.png")
plt.close()

# 3. Scatter
plt.figure()
plt.scatter(df['date'], df['price'])
plt.title("Scatter Plot")
plt.xticks(rotation=45)
plt.savefig("price_scatter.png")
plt.close()

# 4. Rolling average
df['rolling'] = df['price'].rolling(5).mean()
plt.figure()
plt.plot(df['date'], df['price'], label="Price")
plt.plot(df['date'], df['rolling'], label="Rolling Avg")
plt.legend()
plt.title("Rolling Average")
plt.xticks(rotation=45)
plt.savefig("rolling_avg.png")
plt.close()

# 5. Box plot
plt.figure()
plt.boxplot(df['price'])
plt.title("Box Plot")
plt.savefig("box_plot.png")
plt.close()

print("✅ All 5 charts created successfully!")
