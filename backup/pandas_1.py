import pandas as pd
import numpy as np
import datetime
import random
import uuid # For more unique looking IDs if preferred, though simple integers are fine

# --- Configuration ---
NUM_RECORDS = 10000
START_DATE = datetime.datetime(2023, 1, 1)
NUM_DAYS_RANGE = 90 # Generate data over a 3-month period

# NYC Specific Locations
nyc_downtown_zones = ["Financial District", "Midtown Manhattan", "SoHo", "Greenwich Village"]
nyc_airport_zones = ["JFK Airport", "LaGuardia Airport (LGA)", "Newark Liberty Airport (EWR)"] # EWR is NJ but common for NYC
nyc_suburb_zones = [ # Representing outer boroughs or less central areas
    "Forest Hills (Queens)", "Riverdale (Bronx)", "Park Slope (Brooklyn)",
    "Flushing (Queens)", "Upper East Side (Manhattan)", "Williamsburg (Brooklyn)",
    "Staten Island (Residential)", "Long Island City (Queens)", "Harlem (Manhattan)",
    "Bay Ridge (Brooklyn)", "The Bronx (Residential)"
]
all_zones = nyc_downtown_zones + nyc_airport_zones + nyc_suburb_zones

# Driver and Customer Pools
NUM_UNIQUE_DRIVERS = 500
NUM_UNIQUE_CUSTOMERS = 3000

driver_ids_pool = [f"DRV_{str(uuid.uuid4())[:6].upper()}" for _ in range(NUM_UNIQUE_DRIVERS)]
customer_ids_pool = [f"CUST_{str(uuid.uuid4())[:7].upper()}" for _ in range(NUM_UNIQUE_CUSTOMERS)]

# --- Helper Functions ---
def random_timeshift(base_time, max_minutes):
    return base_time + datetime.timedelta(minutes=random.randint(1, max_minutes))

# --- Data Generation ---
data = []

for i in range(NUM_RECORDS):
    # 1. Ride_ID
    ride_id = i + 1001 # Start from 1001 for example

    # 4. Ride_Request_Time
    random_day_offset = random.randint(0, NUM_DAYS_RANGE -1)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    ride_request_time = START_DATE + datetime.timedelta(
        days=random_day_offset,
        hours=random_hour,
        minutes=random_minute,
        seconds=random_second
    )

    # 5. Pickup_Time (1 to 15 minutes after request)
    pickup_time = ride_request_time + datetime.timedelta(minutes=random.randint(1, 15))

    # 3. Distance (in miles)
    # Skew towards shorter rides, but allow some longer ones (e.g., to/from airport)
    if random.random() < 0.1: # 10% chance of a longer ride (e.g. airport)
        distance = round(np.random.uniform(10, 35), 2)
    else:
        distance = round(np.random.uniform(0.5, 12), 2)

    # 6. Dropoff_Time (based on distance + traffic factor)
    # Assuming average speed between 10-30 mph in NYC depending on traffic
    # (Distance / Speed_mph) * 60 = minutes
    avg_speed_mph = np.random.uniform(8, 25)
    ride_duration_minutes = int((distance / avg_speed_mph) * 60) + random.randint(0, 20) # Add traffic variance
    ride_duration_minutes = max(5, ride_duration_minutes) # Minimum 5 min ride
    dropoff_time = pickup_time + datetime.timedelta(minutes=ride_duration_minutes)

    # 2. Fare
    # Basic model: base_fare + (distance_rate * distance) + (time_rate * duration_minutes) + surge_noise
    base_fare_val = np.random.uniform(2.5, 5.0)
    distance_rate = np.random.uniform(1.5, 3.0)
    time_rate = np.random.uniform(0.2, 0.6)
    surge_noise = np.random.uniform(-1.0, 10.0) if random.random() < 0.2 else 0 # 20% chance of some surge/discount noise
    fare = round(base_fare_val + (distance_rate * distance) + (time_rate * (ride_duration_minutes / 60)) + surge_noise, 2)
    fare = max(5.0, fare) # Minimum fare

    # 7. Source_Zone & 8. Destination_Zone
    source_zone = random.choice(all_zones)
    destination_zone = random.choice(all_zones)
    # Ensure destination is not the same as source for most rides (optional, but more realistic)
    while destination_zone == source_zone and random.random() < 0.95: # 95% chance to reroll if same
         destination_zone = random.choice(all_zones)


    # 9. Driver_Rating_by_Customer (skewed towards 4s and 5s)
    driver_rating = np.random.choice([1, 2, 3, 4, 5], p=[0.02, 0.03, 0.15, 0.4, 0.4])

    # 10. Ride_Status & 11. Cancelled_By
    ride_status_options = ["Completed", "Cancelled_by_Customer", "Cancelled_by_Driver", "No_Show_Customer"]
    # Probabilities: Completed much more likely
    ride_status_probs = [0.88, 0.06, 0.04, 0.02]
    ride_status = np.random.choice(ride_status_options, p=ride_status_probs)

    cancelled_by = None
    if ride_status == "Cancelled_by_Customer":
        cancelled_by = "Customer"
    elif ride_status == "Cancelled_by_Driver":
        cancelled_by = "Driver"
    elif ride_status == "No_Show_Customer": # Could also be "Customer" or "System"
        cancelled_by = "Customer"
    # If "Completed", cancelled_by remains None

    # 12. Driver_ID
    driver_id = random.choice(driver_ids_pool)

    # 13. Customer_ID
    customer_id = random.choice(customer_ids_pool)


    data.append([
        ride_id,
        fare,
        distance,
        ride_request_time,
        pickup_time,
        dropoff_time,
        source_zone,
        destination_zone,
        driver_rating, # This is the rating given by customer TO the driver for THIS ride
        ride_status,
        cancelled_by,
        driver_id,
        customer_id
    ])

# --- Create DataFrame ---
columns = [
    "Ride_ID", "Fare", "Distance_Miles",
    "Ride_Request_Time", "Pickup_Time", "Dropoff_Time",
    "Source_Zone", "Destination_Zone",
    "Driver_Rating_by_Customer", # Renamed for clarity from your original "Customer_Rating_of_Driver"
    "Ride_Status", "Cancelled_By",
    "Driver_ID", "Customer_ID"
]
df = pd.DataFrame(data, columns=columns)

# --- Post-processing/Checks (Optional) ---
# Ensure correct data types for timestamps if they aren't already
df['Ride_Request_Time'] = pd.to_datetime(df['Ride_Request_Time'])
df['Pickup_Time'] = pd.to_datetime(df['Pickup_Time'])
df['Dropoff_Time'] = pd.to_datetime(df['Dropoff_Time'])

# Calculate Ride_Duration (for your analytics, good to have)
df['Ride_Duration_Minutes'] = (df['Dropoff_Time'] - df['Pickup_Time']).dt.total_seconds() / 60
df['Ride_Duration_Minutes'] = df['Ride_Duration_Minutes'].round(2)

# Reorder columns to put derived Ride_Duration_Minutes next to time columns
cols_order = [
    "Ride_ID", "Fare", "Distance_Miles",
    "Ride_Request_Time", "Pickup_Time", "Dropoff_Time", "Ride_Duration_Minutes",
    "Source_Zone", "Destination_Zone",
    "Driver_Rating_by_Customer",
    "Ride_Status", "Cancelled_By",
    "Driver_ID", "Customer_ID"
]
df = df[cols_order]


# --- Output ---
print(df.head())
print(f"\nGenerated {len(df)} records.")
print("\nZone Counts (Source):")
print(df['Source_Zone'].value_counts().head())
print("\nRide Status Counts:")
print(df['Ride_Status'].value_counts())
print("\nCancelled By Counts:")
print(df['Cancelled_By'].value_counts(dropna=False)) # include NaNs for non-cancelled

# Save to CSV
df.to_csv("nyc_ride_hailing_data.csv", index=False)
print("\nData saved to nyc_ride_hailing_data.csv")

