import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "users.csv")

class User:
	"""Simple User profile class.

	Attributes:
		first_name (str): User's first name
		last_name (str): User's last name
		email (str): Optional email address
		age (int|None): Optional age
		location (str): Optional location
	"""

	CSV_FILE = "users.csv"

	def __init__(self, first_name, last_name, email="", age=None, location=""):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.age = age
		self.location = location
		# Programming Exercise 2: track login attempts
		self.login_attempts = 0

	def describe_user(self):
		"""Print a summary of the user's information."""
		full_name = f"{self.first_name} {self.last_name}"
		print(f"User: {full_name}")
		if self.age is not None:
			print(f"Age: {self.age}")
		if self.email:
			print(f"Email: {self.email}")
		if self.location:
			print(f"Location: {self.location}")

	def greet_user(self):
		"""Print a personalized greeting to the user."""
		print(f"Hello, {self.first_name}! Welcome back.")

	def increment_login_attempts(self):
		"""Increment the login_attempts by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset the login_attempts to 0."""
		self.login_attempts = 0

	def save_to_csv(self):
		"""Save user details to a CSV file."""
		file_exists = os.path.isfile(self.CSV_FILE)
		
		with open(self.CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
			fieldnames = ['first_name', 'last_name', 'email', 'age', 'location']
			writer = csv.DictWriter(file, fieldnames=fieldnames)
			
			# Write header only if file doesn't exist
			if not file_exists:
				writer.writeheader()
			
			# Write user data
			writer.writerow({
				'first_name': self.first_name,
				'last_name': self.last_name,
				'email': self.email,
				'age': self.age if self.age is not None else '',
				'location': self.location
			})
		
		print(f"User {self.first_name} {self.last_name} saved to {self.CSV_FILE}")


if __name__ == "__main__":
	# Load users from the local users.csv and display each without
	# writing back to avoid redundancy.
	users = []

	if os.path.isfile(csv_path):
		with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
			reader = csv.DictReader(file)
			for row in reader:
				age = int(row['age']) if row.get('age') else None
				user = User(
					row.get('first_name', ''),
					row.get('last_name', ''),
					email=row.get('email', ''),
					age=age,
					location=row.get('location', '')
				)
				users.append(user)
	else:
		print(f"CSV file not found at {csv_path}. Please create `users.csv` in this folder first.")

	# Show each user only when iterating (no redundant CSV writes)
	for u in users:
		u.describe_user()
		u.greet_user()
		print("-" * 40)

	# Programming Exercise 2 demo: incrementing and resetting login attempts
	print("\n--- Programming Exercise 2 Demo (login_attempts) ---\n")
	# Use first loaded user for demo if available, otherwise create a sample
	if users:
		demo = users[0]
	else:
		demo = User("Demo", "User", email="demo@example.com")

	print(f"Demo user: {demo.first_name} {demo.last_name}")

	# Call increment several times and print the value each time
	demo.increment_login_attempts()
	print(f"Login attempts: {demo.login_attempts}")

	demo.increment_login_attempts()
	print(f"Login attempts: {demo.login_attempts}")

	demo.increment_login_attempts()
	print(f"Login attempts: {demo.login_attempts}")

	# Reset to 0 and print
	demo.reset_login_attempts()
	print(f"Login attempts after reset: {demo.login_attempts}")

