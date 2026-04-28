import pandas as pd

def process_inventory():
    file_name = input("Enter File name: ")
    try:
        df = pd.read_csv(file_name)

        df['Discounted_Price'] = df['Price'] * 0.8
        print("Discounted inventory:")
        print(df)

    except FileNotFoundError:
        print("File not found. Please Check filename")
    except Exception as e:
        print(f"an error occurred: {e}")

if __name__ == "__main__":
    process_inventory()