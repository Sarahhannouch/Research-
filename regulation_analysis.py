import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("../Data/regulatory_events.csv")

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(x="Year", y="Market Cap (Trillions USD)", data=df, marker="o")
for i, row in df.iterrows():
    plt.text(row["Year"], row["Market Cap (Trillions USD)"] + 0.05, row["Event"], rotation=45, ha="right")

plt.title("Cryptocurrency Market Cap vs Regulatory Events (2017–2024)")
plt.xlabel("Year")
plt.ylabel("Market Cap (Trillions USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("../charts/market_cap_vs_regulation.png")
plt.show()
