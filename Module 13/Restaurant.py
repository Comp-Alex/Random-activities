import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "restaurants.csv")

class Restaurant:
	"""Restaurant class to store and manage restaurant information.

	Attributes:
		restaurant_name (str): Name of the restaurant
		cuisine_type (str): Type of cuisine served
	"""

	CSV_FILE = "restaurants.csv"

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Print the restaurant's name and cuisine type."""
		print(f"Restaurant: {self.restaurant_name}")
		print(f"Cuisine Type: {self.cuisine_type}")

	def open_restaurant(self):
		"""Print a message indicating that the restaurant is open."""
		print(f"{self.restaurant_name} is now open!")

	def save_to_csv(self):
		"""Save restaurant details to a CSV file."""
		file_exists = os.path.isfile(self.CSV_FILE)
		
		with open(self.CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
			fieldnames = ['restaurant_name', 'cuisine_type']
			writer = csv.DictWriter(file, fieldnames=fieldnames)
			
			# Write header only if file doesn't exist
			if not file_exists:
				writer.writeheader()
			
			# Write restaurant data
			writer.writerow({
				'restaurant_name': self.restaurant_name,
				'cuisine_type': self.cuisine_type
			})
		
		print(f"Restaurant {self.restaurant_name} saved to {self.CSV_FILE}")


if __name__ == "__main__":
	# Load users from the local users.csv and display each without
	# writing back to avoid redundancy.
	users = []

	if os.path.isfile(csv_path):
		with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
			reader = csv.DictReader(file)
			for row in reader:
				restaurant = Restaurant(
					restaurant_name=row['restaurant_name'],
					cuisine_type=row['cuisine_type']
				)
				users.append(restaurant)
	else:
		print(f"CSV file not found at {csv_path}. Please create `users.csv` in this folder first.")

	# Show each user only when iterating (no redundant CSV writes)
	for u in users:
		u.describe_restaurant()
		u.open_restaurant()
		print("-" * 40)
