import pandas as pd

# Load the data
def load_data(file_path):
    return pd.read_csv(file_path)

# Clean the data
def clean_data(df):
    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

if __name__ == "__main__":
    data = load_data('../data/demand_data.csv')
    cleaned_data = clean_data(data)
    print("Cleaned Data:")
    print(cleaned_data.head())
