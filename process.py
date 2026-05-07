import pandas as pd
import os

# Step 1: Define data path
data_path = "data/raw"

# Step 2: Load all CSV files
files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

df_list = []

for file in files:
    file_path = os.path.join(data_path, file)
    df = pd.read_csv(file_path)
    df_list.append(df)

# Step 3: Combine all data
df = pd.concat(df_list, ignore_index=True)

# Step 4: Basic inspection
print("Initial shape:", df.shape)

# Step 5: Convert datetime
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# Step 6: Create ride_length (in minutes)
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# Step 7: Create day_of_week
df['day_of_week'] = df['started_at'].dt.day_name()

# Step 8: Remove invalid rides (negative or zero duration)
df = df[df['ride_length'] > 0]

# Step 9: Drop duplicates
df = df.drop_duplicates()

# Step 10: Drop unnecessary nulls (critical columns only)
df = df.dropna(subset=['started_at', 'ended_at', 'member_casual'])

print("Cleaned shape:", df.shape)

# Step 11: Save cleaned data
output_path = "data/processed/cleaned_data.csv"
df.to_csv(output_path, index=False)

print("Data processing completed. File saved to:", output_path)