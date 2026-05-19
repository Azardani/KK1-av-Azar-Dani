import pandas as pd
df = pd.read_csv("Cars_datasets.csv", encoding="latin1")

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])  
# konverterar Price till nummer
# ogiltiga värden (text, saknade värden osv) blir NaN
# och tas sedan bort


Most_expesnsive = (df["Price"].max())
Least_expesnsive = (df["Price"].min())
average_price = (df["Price"].mean())

most_miles = (df["Mileage"].max())
least_miles = (df["Mileage"].min())
average_miles = (df["Mileage"].mean())

newest_car = (df["Year"].max())
oldest_car = (df["Year"].min())
average_age = (df["Year"].mean())