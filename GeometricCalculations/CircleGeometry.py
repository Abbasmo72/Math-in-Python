import math

# Function to calculate the area and circumference of a circle in centimeters
def calculate_circle(radius_cm):
    area_cm2 = math.pi * radius_cm ** 2  # Calculate area in square centimeters
    circumference_cm = 2 * math.pi * radius_cm  # Calculate circumference in centimeters
    return area_cm2, circumference_cm

# Get the radius from the user in centimeters
radius_cm = float(input("Enter the radius of the circle in centimeters: "))

# Calculate area and circumference
area_cm2, circumference_cm = calculate_circle(radius_cm)

# Display the results
print(f"Area of the circle: {area_cm2:.2f} cm²")  # Display area in square centimeters
print(f"Circumference of the circle: {circumference_cm:.2f} cm")  # Display circumference in centimeters
