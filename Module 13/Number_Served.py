import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "restaurants.csv")

class Restaurant:
	"""Restaurant class to store and manage restaurant information.

	Attributes:
		restaurant_name (str): Name of the restaurant
		cuisine_type (str): Type of cuisine served
		number_served (int): Number of customers served (default: 0)
	"""

	CSV_FILE = "restaurants.csv"

	def __init__(self, restaurant_name, cuisine_type, number_served=0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served

	def describe_restaurant(self):
		"""Print the restaurant's name and cuisine type."""
		print(f"Restaurant: {self.restaurant_name}")
		print(f"Cuisine Type: {self.cuisine_type}")

	def open_restaurant(self):
		"""Print a message indicating that the restaurant is open."""
		print(f"{self.restaurant_name} is now open!")

	def set_number_served(self, number):
		"""Set the number of customers that have been served."""
		self.number_served = number
		print(f"Number of customers served: {self.number_served}")

	def increment_number_served(self, number):
		"""Increment the number of customers served."""
		self.number_served += number
		print(f"Number of customers served: {self.number_served}")

	def save_to_csv(self):
		"""Save restaurant details to a CSV file."""
		file_exists = os.path.isfile(self.CSV_FILE)
		
		with open(self.CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
			fieldnames = ['restaurant_name', 'cuisine_type', 'number_served']
			writer = csv.DictWriter(file, fieldnames=fieldnames)
			
			# Write header only if file doesn't exist
			if not file_exists:
				writer.writeheader()
			
			# Write restaurant data
			writer.writerow({
				'restaurant_name': self.restaurant_name,
				'cuisine_type': self.cuisine_type,
				'number_served': self.number_served
			})
		
		print(f"Restaurant {self.restaurant_name} saved to {self.CSV_FILE}")


if __name__ == "__main__":
	# Load restaurants from the local restaurants.csv
	restaurants = []

	if os.path.isfile(csv_path):
		with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
			reader = csv.DictReader(file)
			for row in reader:
				number_served = int(row.get('number_served', 0)) if row.get('number_served') else 0
				restaurant = Restaurant(
					row.get('restaurant_name', ''),
					row.get('cuisine_type', ''),
					number_served=number_served
				)
				restaurants.append(restaurant)
	else:
		print(f"CSV file not found at {csv_path}. Please run Restaurant.py first to create restaurants.")
	
	# Test number_served functionality with all loaded restaurants
	print("\n--- Programming Exercise 4: Number Served ---\n")
	for restaurant in restaurants:
		print(f"Restaurant: {restaurant.restaurant_name}")
		print(f"Initial number of customers served: {restaurant.number_served}\n")
		
		# Change the number and print it again
		print("Setting number served to 50.")
		restaurant.set_number_served(50)
		print()
		
		# Increment the number of customers served
		print("Incrementing number served by 25.")
		restaurant.increment_number_served(25)
		print()
		
		# Increment again for a day of business
		print("Incrementing number served by 30.")
		restaurant.increment_number_served(30)
		print()
		
		print("-" * 40 + "\n")
