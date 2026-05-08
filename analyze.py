import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_data.csv")

print("Dataset shape:", df.shape)
print(df.head())
print(df.columns)

# Average ride length by user type
avg_ride = df.groupby('member_casual')['ride_length'].mean()
print("\nAverage Ride Length (minutes):")
print(avg_ride)

# Total rides by user type
ride_count = df['member_casual'].value_counts()
print("\nRide Count:")
print(ride_count)

# Rides by day of week
rides_by_day = df.groupby(['day_of_week', 'member_casual']).size().reset_index(name='count')
print("\nRides by Day of Week:")
print(rides_by_day)

avg_by_day = df.groupby(['day_of_week', 'member_casual'])['ride_length'].mean().reset_index()
print("\nAverage Ride Length by Day:")
print(avg_by_day)

