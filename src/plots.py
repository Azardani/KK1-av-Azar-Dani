import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("car_price_dataset.csv", sep=";")


plt.scatter(df["Mileage"], df["Price"])

plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Mileage vs Price")

# sparar bilden
plt.savefig("price_vs_mileage.png", dpi=300, bbox_inches="tight")


plt.show()