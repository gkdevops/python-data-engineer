import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np # For potential numerical operations if needed

# --- Configuration ---
DATA_FILE = "nyc_ride_hailing_data.csv"
TOP_N_POPULAR = 10 # For showing top N routes/zones

# --- Load Data ---
try:
    df = pd.read_csv(DATA_FILE, parse_dates=['Ride_Request_Time', 'Pickup_Time', 'Dropoff_Time'])
except FileNotFoundError:
    print(f"Error: The file '{DATA_FILE}' was not found. Please generate it first.")
    exit()

print("--- Data Loaded Successfully ---")
print(f"Shape of the dataset: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())
print("\nData Info:")
df.info()

# --- 1. Average Fare, Distance, Ride Duration ---
print("\n\n--- 1. Average Fare, Distance, Ride Duration ---")
avg_fare = df['Fare'].mean()
avg_distance = df['Distance_Miles'].mean()
avg_ride_duration = df['Ride_Duration_Minutes'].mean() # Assuming this was calculated in generation

print(f"Average Fare: ${avg_fare:.2f}")
print(f"Average Distance: {avg_distance:.2f} miles")
print(f"Average Ride Duration: {avg_ride_duration:.2f} minutes")

# --- 2. Most Popular Routes, Pickup/Drop-off Zones ---
print(f"\n\n--- 2. Most Popular Routes & Zones (Top {TOP_N_POPULAR}) ---")

# Popular Pickup Zones
popular_pickup_zones = df['Source_Zone'].value_counts().head(TOP_N_POPULAR)
print("\nMost Popular Pickup Zones:")
print(popular_pickup_zones)

plt.figure(figsize=(10, 6))
sns.barplot(y=popular_pickup_zones.index, x=popular_pickup_zones.values, palette="viridis", hue=popular_pickup_zones.index, legend=False)
plt.title(f'Top {TOP_N_POPULAR} Most Popular Pickup Zones')
plt.xlabel('Number of Rides')
plt.ylabel('Zone')
plt.tight_layout()
plt.show()

# Popular Drop-off Zones
popular_dropoff_zones = df['Destination_Zone'].value_counts().head(TOP_N_POPULAR)
print("\nMost Popular Drop-off Zones:")
print(popular_dropoff_zones)

plt.figure(figsize=(10, 6))
sns.barplot(y=popular_dropoff_zones.index, x=popular_dropoff_zones.values, palette="mako", hue=popular_dropoff_zones.index, legend=False)
plt.title(f'Top {TOP_N_POPULAR} Most Popular Drop-off Zones')
plt.xlabel('Number of Rides')
plt.ylabel('Zone')
plt.tight_layout()
plt.show()

# Popular Routes (Source -> Destination)
df['Route'] = df['Source_Zone'] + " to " + df['Destination_Zone']
popular_routes = df['Route'].value_counts().head(TOP_N_POPULAR)
print("\nMost Popular Routes:")
print(popular_routes)

plt.figure(figsize=(12, 7))
sns.barplot(y=popular_routes.index, x=popular_routes.values, palette="cubehelix", hue=popular_routes.index, legend=False)
plt.title(f'Top {TOP_N_POPULAR} Most Popular Routes')
plt.xlabel('Number of Rides')
plt.ylabel('Route (Source to Destination)')
plt.tight_layout()
plt.show()

# --- 3. Busiest Times of Day/Week ---
print("\n\n--- 3. Busiest Times of Day/Week ---")

# Busiest Hour of Day
df['Hour_of_Day'] = df['Ride_Request_Time'].dt.hour
busiest_hours = df['Hour_of_Day'].value_counts().sort_index()
print("\nRides by Hour of Day:")
print(busiest_hours)

plt.figure(figsize=(12, 6))
sns.barplot(x=busiest_hours.index, y=busiest_hours.values, color="skyblue")
plt.title('Number of Rides by Hour of Day')
plt.xlabel('Hour of Day (0-23)')
plt.ylabel('Number of Rides')
plt.xticks(range(0, 24))
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# Busiest Day of Week
df['Day_of_Week'] = df['Ride_Request_Time'].dt.day_name()
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
busiest_days = df['Day_of_Week'].value_counts().reindex(days_order)
print("\nRides by Day of Week:")
print(busiest_days)

plt.figure(figsize=(10, 6))
sns.barplot(x=busiest_days.index, y=busiest_days.values, palette="crest", hue=busiest_days.index, legend=False)
plt.title('Number of Rides by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Rides')
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()


# --- 4. Distribution of Driver/Customer Ratings ---
# Assuming 'Driver_Rating_by_Customer' is the rating customer gave to driver for this ride
print("\n\n--- 4. Distribution of Driver Ratings (Given by Customers) ---")
rating_distribution = df['Driver_Rating_by_Customer'].value_counts().sort_index()
print(rating_distribution)

plt.figure(figsize=(8, 5))
sns.countplot(x='Driver_Rating_by_Customer', data=df, palette="YlGnBu", hue='Driver_Rating_by_Customer', legend=False, order=sorted(df['Driver_Rating_by_Customer'].unique()))
plt.title('Distribution of Driver Ratings (Given by Customers)')
plt.xlabel('Rating (1-5 Stars)')
plt.ylabel('Number of Rides')
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# --- 5. Cancellation Rates ---
print("\n\n--- 5. Cancellation Rates ---")
total_rides = len(df)

# Identify cancelled rides
# Assuming "Completed" is the only non-cancelled status for simplicity based on generation script
# More robust: check for statuses that explicitly mean cancellation
cancelled_rides_df = df[~df['Ride_Status'].str.contains("Completed", case=False, na=False)]
num_cancelled_rides = len(cancelled_rides_df)

if total_rides > 0:
    overall_cancellation_rate = (num_cancelled_rides / total_rides) * 100
    print(f"Overall Cancellation Rate: {overall_cancellation_rate:.2f}% ({num_cancelled_rides} out of {total_rides} rides)")
else:
    print("No rides in the dataset to calculate cancellation rate.")

# Breakdown of cancellations by reason/source (Cancelled_By column)
if num_cancelled_rides > 0:
    cancellation_reasons = cancelled_rides_df['Cancelled_By'].value_counts(dropna=False) # include NaN if 'Cancelled_By' can be missing for cancellations
    print("\nBreakdown of Cancellations by Source:")
    print(cancellation_reasons)

    cancellation_reasons_percentage = cancelled_rides_df['Cancelled_By'].value_counts(normalize=True, dropna=False) * 100
    print("\nBreakdown of Cancellations by Source (Percentage of Cancelled Rides):")
    print(cancellation_reasons_percentage)


    plt.figure(figsize=(8, 5))
    sns.barplot(x=cancellation_reasons.index.astype(str), y=cancellation_reasons.values, palette="Reds_r", hue=cancellation_reasons.index.astype(str), legend=False) # astype(str) for NaN handling
    plt.title('Breakdown of Ride Cancellations by Source')
    plt.xlabel('Cancelled By')
    plt.ylabel('Number of Cancelled Rides')
    plt.tight_layout()
    plt.show()
else:
    print("No cancelled rides found.")


print("\n\n--- Descriptive Analytics Complete ---")
