import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/processed/cleaned_data.csv")

# Style
sns.set(style="whitegrid")

# -------------------------------
# 1. Average Ride Length
# -------------------------------
plt.figure()
avg_ride = df.groupby('member_casual')['ride_length'].mean().reset_index()
sns.barplot(data=avg_ride, x='member_casual', y='ride_length')
plt.title("Average Ride Length by User Type")
plt.xlabel("User Type")
plt.ylabel("Ride Length (minutes)")
plt.savefig("data/docs/avg_ride_length.png")
plt.close()

# -------------------------------
# 2. Ride Count
# -------------------------------
plt.figure()
ride_count = df['member_casual'].value_counts().reset_index()
ride_count.columns = ['member_casual', 'count']
sns.barplot(data=ride_count, x='member_casual', y='count')
plt.title("Total Rides by User Type")
plt.xlabel("User Type")
plt.ylabel("Number of Rides")
plt.savefig("data/docs/ride_count.png")
plt.close()

# -------------------------------
# 3. Rides by Day of Week
# -------------------------------
plt.figure()
rides_by_day = df.groupby(['day_of_week', 'member_casual']).size().reset_index(name='count')

# Order days correctly
order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

sns.barplot(data=rides_by_day, x='day_of_week', y='count', hue='member_casual', order=order)
plt.title("Rides by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Rides")
plt.xticks(rotation=45)
plt.savefig("data/docs/rides_by_day.png")
plt.close()

# -------------------------------
# 4. Avg Ride Length by Day
# -------------------------------
plt.figure()
avg_by_day = df.groupby(['day_of_week', 'member_casual'])['ride_length'].mean().reset_index()

sns.barplot(data=avg_by_day, x='day_of_week', y='ride_length', hue='member_casual', order=order)
plt.title("Average Ride Length by Day")
plt.xlabel("Day")
plt.ylabel("Ride Length (minutes)")
plt.xticks(rotation=45)
plt.savefig("data/docs/avg_by_day.png")
plt.close()

print("Visualizations created successfully.")