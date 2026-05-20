import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("car_price_dataset.csv", sep=";")

df["Score"] = 0

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])  
# konverterar Price till nummer
# ogiltiga värden (text, saknade värden osv) blir NaN
# och tas sedan bort




df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Mileage"] = pd.to_numeric(df["Mileage"], errors="coerce")
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

df = df.dropna(subset=["Price", "Mileage", "Year"])


Most_expensive = df[df["Price"] == df["Price"].max()]
Least_expensive = df[df["Price"] == df["Price"].min()]

average_price = df["Price"].mean()

most_miles = df[df["Mileage"] == df["Mileage"].max()]
least_miles = df[df["Mileage"] == df["Mileage"].min()]

average_miles = df["Mileage"].mean()

newest_car = df[df["Year"] == df["Year"].max()]
oldest_car = df[df["Year"] == df["Year"].min()]

average_age = df["Year"].mean()


cheap_cars = df[df["Price"] < average_price]
expensive_cars = df[df["Price"] > average_price]

high_mileage = df[df["Mileage"] > average_miles]
low_mileage = df[df["Mileage"] < average_miles]

old_cars = df[df["Year"] < average_age]
new_cars = df[df["Year"] > average_age]


df["Score"] = 0

df.loc[df["Mileage"] < average_miles, "Score"] += 1
df.loc[df["Mileage"] > average_miles, "Score"] -= 1

df.loc[df["Year"] > average_age, "Score"] += 1
df.loc[df["Year"] < average_age, "Score"] -= 1

df.loc[df["Price"] < average_price, "Score"] += 1
df.loc[df["Price"] > average_price, "Score"] -= 1


Very_good_cars = df[df["Score"] >= 2]
good_cars = df[df["Score"] == 1]
neutral_cars = df[df["Score"] == 0]
bad_cars = df[df["Score"] <= -1]

