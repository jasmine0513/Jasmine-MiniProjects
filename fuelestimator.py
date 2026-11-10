import pandas as pd

filename = input("Enter CSV file: ")
df = pd.read_csv(filename)

df["Fuel_Cost"] = (df["Distance_miles"] / df["MPG"] * df["Price_per_gallon"])
df["Price_per_mile"] = (df["Price_per_gallon"] / df["MPG"])

print("Fuel costs:")
print(df)
