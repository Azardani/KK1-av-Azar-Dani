import pandas as pd
df = pd.read_csv("Cars_datasets.csv", encoding="latin1")

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])  
# konverterar Price till nummer
# ogiltiga värden (text, saknade värden osv) blir NaN
# och tas sedan bort


print(df.columns)



