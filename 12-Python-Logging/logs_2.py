import logging

# Configure basic logging with a slightly more informative format
logging.basicConfig(
    level=logging.INFO,  # Only log warnings and above
    format='%(levelname)s: %(message)s'
)

def check_temperature(temperature):
    """Checks the temperature and logs a message based on its value."""
    logging.debug(f"Checking temperature: {temperature}°C")
    if temperature > 30:
        logging.warning(f"Temperature is high: {temperature}°C. Consider taking precautions.")
    elif temperature < 10:
        logging.warning(f"Temperature is low: {temperature}°C. Dress warmly.")
    else:
        logging.info(f"Temperature is comfortable: {temperature}°C.")

def calculate_area(length, width):
    """Calculates the area of a rectangle and logs the dimensions."""
    logging.debug(f"Calculating area for length={length}, width={width}")
    if length < 0 or width < 0:
        logging.error("Invalid dimensions! Length and width must be non-negative.")
        return None
    area = length * width
    logging.info(f"Area of rectangle: {area}")
    return area

def main():
    """Main function demonstrating temperature check and area calculation."""
    check_temperature(35)
    check_temperature(5)
    check_temperature(20)

    area1 = calculate_area(5, 10)
    print(f"Area 1: {area1}")

    area2 = calculate_area(-2, 8)
    print(f"Area 2: {area2}")

if __name__ == "__main__":
    main()
