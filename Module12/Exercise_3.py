import csv
import os

# Country CSV Writer Program
# Creates a CSV file with country data using the csv module

country_file = os.path.join(os.path.dirname(__file__), "countries.csv")

# Define fieldnames for the CSV
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# Define country data
rows = [
    {'name': 'Albania', 'area': 28748, 'country_code2': 'AL', 'country_code3': 'ALB'},
    {'name': 'Algeria', 'area': 2381741, 'country_code2': 'DZ', 'country_code3': 'DZA'},
    {'name': 'American Samoa', 'area': 199, 'country_code2': 'AS', 'country_code3': 'ASM'}
]

# Write to CSV file
with open(country_file, 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Country data written to {country_file}")

# Read and display the CSV file
print("\n=== CSV File Contents ===\n")
with open(country_file, 'r', encoding='UTF8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Name: {row['name']}, Area: {row['area']}, Code2: {row['country_code2']}, Code3: {row['country_code3']}")
