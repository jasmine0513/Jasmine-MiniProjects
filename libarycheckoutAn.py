"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""

import pandas as pd

def analyze_library_data():
    file_name = input("Enter CSV file name: ")
    
    try:
        df = pd.read_csv(file_name)
        attribute = input("Enter attribute: ")
        
        if attribute in df.columns:
            top_5 = df[attribute].value_counts().head(5)
            print(f"The top 5 values for {attribute} are:")
            print(top_5)
        else:
            print(f"Attribute '{attribute}' not found in the dataset.")
            
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    analyze_library_data()
