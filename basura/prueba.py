import numpy as np

# Input
age = float(input("Enter the age in years (18.0 to 74.9): "))
body_fat_percentage = float(input("Enter the body fat percentage (5 to 95): "))

age_ranges = [
    (18.0, 24.9),
    (25.0, 29.9),
    (30.0, 34.9),
    (35.0, 39.9),
    (40.0, 44.9),
    (45.0, 49.9),
    (50.0, 54.9),
    (55.0, 59.9),
    (60.0, 64.9),
    (65.0, 69.9),
    (70.0, 74.9)
]

# Define body fat percentage ranges
body_fat_ranges = [5, 10, 15, 25, 50, 75, 85, 90, 95]

# Find the closest body fat percentage
closest_body_fat = min(body_fat_ranges, key=lambda x: abs(x - body_fat_percentage))