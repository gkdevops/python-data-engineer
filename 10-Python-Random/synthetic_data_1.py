#!/usr/bin/env python3
"""
Generate a synthetic ride-sharing CSV with 10 000 rows
Columns: source, destination, fare_usd, distance_km, driver_gender, ride_type, customer_name
"""

import csv
import random
from faker import Faker

fake = Faker()
random.seed(42)
Faker.seed(42)

# ---------- Configurable parameters ----------
NUM_ROWS        = 10_000
OUTFILE         = "rides.csv"
CITIES          = ["New York", "Chicago", "San Francisco", "Boston",
                   "Los Angeles", "Seattle", "Austin", "Denver",
                   "Miami", "Atlanta", "Houston", "Phoenix"]
GENDERS         = ["Male", "Female"]
RIDE_TYPES      = ["shared", "individual"]

# ---------- CSV generation ----------
with open(OUTFILE, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["source_city",
                     "destination_city",
                     "fare_usd",
                     "distance_km",
                     "driver_gender",
                     "ride_type",
                     "customer_name"])

    for _ in range(NUM_ROWS):
        # Ensure source != destination
        source, destination = random.sample(CITIES, 2)

        fare     = round(random.uniform(5, 120), 2)      # $5.00–$120.00
        distance = round(random.uniform(1, 60), 2)       # 1–60 km

        gender   = random.choice(GENDERS)
        ride_t   = random.choice(RIDE_TYPES)
        cust     = fake.name()

        writer.writerow([source, destination, fare, distance, gender, ride_t, cust])

print(f"✅  Generated {NUM_ROWS} rows into {OUTFILE}")
