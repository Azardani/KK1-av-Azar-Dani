import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("car_price_dataset.csv", sep=";")



plt.figure(figsize=(8,6))

plt.hist(df["Price"], bins=20)

plt.xlabel("Price")
plt.ylabel("number of cars")
plt.title("price distribution of cars")

plt.tight_layout()

plt.savefig("price_distribution.png", dpi=300, bbox_inches="tight")

plt.show()

plt.scatter(df["Mileage"], df["Price"])

plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Mileage vs Price")

# sparar bilden
plt.savefig("price_vs_mileage.png", dpi=300, bbox_inches="tight")



brand_avg = df.groupby("Brand")["Price"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

bars = plt.bar(brand_avg.index, brand_avg.values)

plt.xlabel("Brand")
plt.ylabel("Average Price")
plt.title("Top 10 Brands by Average Price")

plt.xticks(rotation=45)

# visar värden
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():.0f}",
        ha="center",
        va="bottom"
    )

plt.savefig("Top_10_average", dpi=300, bbox_inches="tight")

plt.tight_layout()
plt.show()
