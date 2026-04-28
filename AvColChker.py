"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""
import sys
import pandas as pd

ALLOWED = ("Temperature", "Luminosity", "Radius", "Absolute Magnitude")

def main():
    fname = input("File name: ").strip()
    col = input(f"Column ({', '.join(ALLOWED)}): ").strip()

    try:
        df = pd.read_csv(fname)
    except Exception as e:
        print("Error reading file:", e)
        sys.exit(1)

    if col not in df.columns:
        print(f"Column '{col}' not found in file.")
        sys.exit(1)

    df[col] = pd.to_numeric(df[col], errors='coerce')
    means = df.groupby('Star type')[col].mean()

    print(f"\nAverage {col} per Star type:\n{means}")


if __name__ == "__main__":
    main()