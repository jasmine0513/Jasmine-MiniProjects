"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""
import pandas as pd

def process_inventory():
    file_name = input("Enter inventory file name: ")
    
    try:
        df = pd.read_csv(file_name)
        df['Discounted_Price'] = df['Price'] * 0.8
        print("\nDiscounted inventory:")
        print(df)

    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_inventory()