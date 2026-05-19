import pandas as pd
df = pd.read_csv("car_price_dataset.csv", sep=";")

df["Score"] = 0

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

Honda_cars = df[df["Brand"] == "Honda"]

Bmw_cars = df[df["Brand"] == "BMW"]



cheap_cars = df[df["Price"]< average_price]
expensive_cars = df[df["Price"] > average_price]
high_mileage = df[df["Mileage"] > average_miles]
low_mileage = df[df["Mileage"] < average_miles]
old_cars = df[df["Year"] < average_age]
new_cars = df[df["Year"] > average_age]

df.loc[df["Mileage"] < average_miles, "Score"] += 1
df.loc[df["Mileage"] > average_miles, "Score"] -= 1
df.loc[df["Year"] < average_age, "Score"] -= 1
df.loc[df["Year"] > average_age, "Score"] += 1
df.loc[df["Price"] < average_price, "Score"] += 1
df.loc[df["Price"] > average_price, "Score"] -= 1


Very_good_cars = df[(df["Mileage"] < average_miles) & (df["Price"] < average_price) & (df["Year"] > average_age)]
Very_bad_cars = df[(df["Mileage"] > average_miles) & (df["Price"] > average_price) & (df["Year"] < average_age)]

Bad_cars = df[df["Score"] == 1]
good_cars = df[df["Score"] == 2]
Very_bad_cars = df[df["Score"] == 0]
Very_good_cars = df[df["Score"] == 3]

print(high_mileage)

