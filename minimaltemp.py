"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""
import pandas as pd

filename = input("Enter CSV file name: ")
df = pd.read_csv(filename)

overall_min = df['MinTemp'].min()
min_by_location = df.groupby('Location')['MinTemp'].min()

print(f"Overall min temp: {overall_min}")
print("\nMinimum temperature by location:")
print(min_by_location)