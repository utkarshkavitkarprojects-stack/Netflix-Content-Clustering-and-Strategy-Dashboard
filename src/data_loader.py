#data_loader.py
# Import the pandas library for working with data
import pandas as pd

# Define a function to load the heart.csv file
def load_data(path='data/raw/NETFLIX MOVIES AND TV SHOWS CLUSTERING.csv'):

    try:
        df = pd.read_csv(path)
        print("✅ Data loaded successfully!")
        return df

    except FileNotFoundError:
        print(f"❌ File not found at: {path}")
        return None

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None