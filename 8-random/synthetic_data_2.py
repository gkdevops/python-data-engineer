import datetime
import random
import numpy as np
import uuid
import csv

# --- Configuration ---
NUM_RECORDS = 10000
START_DATE = datetime.datetime(2023, 1, 1)
NUM_DAYS_RANGE = 90 # Generate data over a 3-month period

# NYC Specific Locations
nyc_downtown_zones = ["Financial District", "Midtown Manhattan", "SoHo", "Greenwich Village"]
nyc_airport_zones = ["JFK Airport", "LaGuardia Airport (LGA)", "Newark Liberty Airport (EWR)"]
nyc_suburb_zones = [
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

# --- Data Generation ---
data = []

for i in range(NUM_RECORDS):
    # 1. Ride_ID
    ride_id = i + 1001

    # 4. Ride_Request_Time
    random_day_offset = random.randint(0, NUM_DAYS_RANGE - 1)
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
    if random.random() < 0.1: # 10% chance of a longer ride
        distance = round(np.random.uniform(10, 35), 2)
    else:
        distance = round(np.random.uniform(0.5, 12), 2)

    # 6. Dropoff_Time (based on distance + traffic factor)
    avg_speed_mph = np.random.uniform(8, 25)
    ride_duration_minutes = int((distance / avg_speed_mph) * 60) + random.randint(0, 20)
    ride_duration_minutes = max(5, ride_duration_minutes)
    dropoff_time = pickup_time + datetime.timedelta(minutes=ride_duration_minutes)

    # 2. Fare
    base_fare_val = np.random.uniform(2.5, 5.0)
    distance_rate = np.random.uniform(1.5, 3.0)
    time_rate = np.random.uniform(0.2, 0.6)
    surge_noise = np.random.uniform(-1.0, 10.0) if random.random() < 0.2 else 0
    fare = round(base_fare_val + (distance_rate * distance) + (time_rate * (ride_duration_minutes / 60)) + surge_noise, 2)
    fare = max(5.0, fare)

    # 7. Source_Zone & 8. Destination_Zone
    source_zone = random.choice(all_zones)
    destination_zone = random.choice(all_zones)
    while destination_zone == source_zone and random.random() < 0.95:
         destination_zone = random.choice(all_zones)

    # 9. Driver_Rating_by_Customer
    driver_rating = np.random.choice([1, 2, 3, 4, 5], p=[0.02, 0.03, 0.15, 0.4, 0.4])

    # 10. Ride_Status & 11. Cancelled_By
    ride_status_options = ["Completed", "Cancelled_by_Customer", "Cancelled_by_Driver", "No_Show_Customer"]
    ride_status_probs = [0.88, 0.06, 0.04, 0.02]
    ride_status = np.random.choice(ride_status_options, p=ride_status_probs)

    cancelled_by = None
    if ride_status == "Cancelled_by_Customer":
        cancelled_by = "Customer"
    elif ride_status == "Cancelled_by_Driver":
        cancelled_by = "Driver"
    elif ride_status == "No_Show_Customer":
        cancelled_by = "Customer"

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
        driver_rating,
        ride_status,
        cancelled_by,
        driver_id,
        customer_id
    ])

# Save to CSV using built-in csv module
columns = [
    "Ride_ID", "Fare", "Distance_Miles",
    "Ride_Request_Time", "Pickup_Time", "Dropoff_Time",
    "Source_Zone", "Destination_Zone",
    "Driver_Rating_by_Customer",
    "Ride_Status", "Cancelled_By",
    "Driver_ID", "Customer_ID"
]

with open("nyc_ride_hailing_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)  # Write header
    writer.writerows(data)    # Write all data rows

print(f"Generated {len(data)} synthetic records")
print("Data saved to nyc_ride_hailing_data.csv")