import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("car_price_dataset.csv", sep=";")


df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])  
# konverterar Price till nummer
# ogiltiga värden (text, saknade värden osv) blir NaN
# och tas sedan bort




df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Mileage"] = pd.to_numeric(df["Mileage"], errors="coerce")
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

df = df.dropna(subset=["Price", "Mileage", "Year"])


Most_expensive = df[df["Price"] == df["Price"].max()]   ## hittar den dyraste samt billigaste bilen
Least_expensive = df[df["Price"] == df["Price"].min()]
average_price = df["Price"].mean() ## genomsnitliga priset av alla bilar

most_miles = df[df["Mileage"] == df["Mileage"].max()] ## mest och minst miltal
least_miles = df[df["Mileage"] == df["Mileage"].min()]
average_miles = df["Mileage"].mean() ## genosnitlliga miltal 

newest_car = df[df["Year"] == df["Year"].max()] ## nyaste och äldsta bilen
oldest_car = df[df["Year"] == df["Year"].min()]
average_age = df["Year"].mean() ## genomsnitts ålder på bilarna


cheap_cars = df[df["Price"] < average_price]  ## alla bilar som kostar mindre än genomsnittet räknas som billiga. 
expensive_cars = df[df["Price"] > average_price]## alla som kostar mer är dyra

high_mileage = df[df["Mileage"] > average_miles] ## högre samt lägre miltal än genomsnittet
low_mileage = df[df["Mileage"] < average_miles] 

old_cars = df[df["Year"] < average_age] ## kollar bilar äldre samt yngre än genomsnitt
new_cars = df[df["Year"] > average_age]


df["Score"] = 0 ## säger att alla bilar har 0 poäng innan deras egenskaper jämförs

## poängsystem där man kan jämföra för och nackdelar med bilarna
## en bil som är äldre än genomsnittet behöver inte vara en dålig bil 
## den kan ha bra egenskaper som att den är billig 
## eller har lågt miltal!
df.loc[df["Mileage"] < average_miles, "Score"] += 1 
df.loc[df["Mileage"] > average_miles, "Score"] -= 1  
df.loc[df["Year"] > average_age, "Score"] += 1
df.loc[df["Year"] < average_age, "Score"] -= 1
df.loc[df["Price"] < average_price, "Score"] += 1
df.loc[df["Price"] > average_price, "Score"] -= 1


too_good_to_be_true_cars = df[df["Score"] == 3]
Very_good_cars = df[df["Score"] >= 2]
good_cars = df[df["Score"] == 1]
neutral_cars = df[df["Score"] == 0]
bad_cars = df[df["Score"] == -1]
Very_bad_cars = df[df["Score"] == -2]
Horrible_cars = df[df["Score"] == -3]



