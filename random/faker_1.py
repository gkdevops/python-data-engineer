import csv
import random
from faker import Faker # For generating more realistic names and locations

# Initialize Faker. You can specify a locale for more region-specific data
fake = Faker()
# For more diverse city names, you can add multiple locales,
# but for simplicity, we'll use the default (often en_US based)
# or explicitly set one.
# fake_de = Faker('de_DE')
# fake_fr = Faker('fr_FR')

# --- Configuration ---
NUM_ROWS = 10000
OUTPUT_CSV_FILE = 'ride_sharing_data.csv'

# --- Data Generation Parameters ---
POSSIBLE_LOCATIONS = [fake.city() for _ in range(100)] + \
                     [fake.street_address() for _ in range(100)] + \
                     [f"{fake.city()} Airport" for _ in range(20)] + \
                     [f"{fake.company()} HQ" for _ in range(30)]
# Ensure we have enough unique locations if NUM_ROWS is very large
# For 10k rows, 250 unique locations should provide good variety.

DRIVER_GENDERS = ['Male', 'Female', 'Non-binary', 'Prefer not to say']
RIDE_TYPES = ['Shared', 'Individual']

# --- Helper Functions ---
def generate_customer_name():
    return fake.name()

def generate_locations():
    """Generates a unique source and destination."""
    source, destination = random.sample(POSSIBLE_LOCATIONS, 2)
    return source, destination

def generate_distance_km():
    """Generates a realistic distance in kilometers."""
    # Skew towards shorter rides, but allow longer ones
    if random.random() < 0.7:  # 70% chance of shorter rides
        return round(random.uniform(1.0, 15.0), 1)
    else:
        return round(random.uniform(15.1, 60.0), 1)

def calculate_fare(distance_km, ride_type):
    """Calculates fare based on distance and ride type."""
    base_fare = 2.50  # Base currency unit (e.g., USD)
    rate_per_km_individual = 1.20
    rate_per_km_shared = 0.85

    if ride_type == 'Individual':
        fare = base_fare + (distance_km * rate_per_km_individual)
    else: # Shared
        fare = base_fare + (distance_km * rate_per_km_shared)

    # Add some minor random fluctuation to make it more realistic
    fare *= random.uniform(0.95, 1.05)
    # Ensure minimum fare
    fare = max(fare, base_fare + 1.0) # Minimum fare slightly above base
    return round(fare, 2)

def generate_driver_gender():
    return random.choice(DRIVER_GENDERS)

def generate_ride_type():
    return random.choice(RIDE_TYPES)

# --- Main Script ---
def generate_csv_data(filename, num_rows):
    header = [
        'Customer Name',
        'Source',
        'Destination',
        'Distance (km)',
        'Ride Type', # Placed here to calculate fare correctly
        'Fare ($)',
        'Driver Gender'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header) # Write the header row

        print(f"Generating {num_rows} rows of data...")
        for i in range(num_rows):
            customer_name = generate_customer_name()
            source, destination = generate_locations()
            distance = generate_distance_km()
            ride_type = generate_ride_type() # Generate ride type before fare
            fare = calculate_fare(distance, ride_type)
            driver_gender = generate_driver_gender()

            row = [
                customer_name,
                source,
                destination,
                distance,
                ride_type,
                fare,
                driver_gender
            ]
            writer.writerow(row)

            if (i + 1) % 1000 == 0: # Print progress
                print(f"Generated {i + 1}/{num_rows} rows...")

    print(f"\nSuccessfully generated {num_rows} rows in '{filename}'")

if __name__ == '__main__':
    # Seed for reproducibility if needed during development/testing
    # random.seed(42)
    # Faker.seed(42) # Note: Faker.seed() seeds the global instance

    generate_csv_data(OUTPUT_CSV_FILE, NUM_ROWS)

