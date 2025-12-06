import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "users.csv")

# Default privileges assigned to Alexander when none exist
DEFAULT_PRIVILEGES = ["can add post", "can delete post"]


class Privileges:
	"""A class to manage administrator privileges.
	
	Attributes:
		privileges (list): List of privilege strings (e.g., "can add post", "can delete post")
	"""
	
	def __init__(self, privileges=None):
		"""Initialize Privileges with a list of privilege strings.
		
		Args:
			privileges (list): List of privilege strings. Defaults to empty list.
		"""
		self.privileges = privileges if privileges is not None else []
	
	def show_privileges(self):
		"""Display the set of privileges."""
		if self.privileges:
			print("Privileges:")
			for privilege in self.privileges:
				print(f"  - {privilege}")
		else:
			print("No privileges assigned.")
	
	def get_privileges(self):
		"""Get the list of privileges.
		
		Returns:
			list: List of privilege strings
		"""
		return self.privileges
	
	def set_privileges(self, privileges):
		"""Set the list of privileges.
		
		Args:
			privileges (list): List of privilege strings
		"""
		self.privileges = privileges


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


class Admin(User):
	"""Administrator user with special privileges.
	
	Inherits from User and adds administrative privileges via Privileges class.
	
	Attributes:
		privileges (Privileges): Instance of Privileges class managing admin privileges
	"""
	
	def __init__(self, first_name, last_name, email="", age=None, location="", privileges=None):
		"""Initialize an Admin user with optional privileges.
		
		Args:
			privileges (list): List of privilege strings. Defaults to empty list.
		"""
		super().__init__(first_name, last_name, email, age, location)
		if privileges is None:
			privileges = []
		self.privileges = Privileges(privileges)
	
	def show_privileges(self):
		"""Display the administrator's set of privileges."""
		print(f"\n{self.first_name} {self.last_name}'s Privileges:")
		self.privileges.show_privileges()
	
	def get_privileges(self):
		"""Get the administrator's privileges.
		
		Returns:
			list: List of privilege strings
		"""
		return self.privileges.get_privileges()
	
	def set_privileges(self, privileges):
		"""Set the administrator's privileges.
		
		Args:
			privileges (list): List of privilege strings
		"""
		self.privileges.set_privileges(privileges)


def display_menu():
	"""Display the main menu options."""
	print("\n" + "=" * 50)
	print("ADMIN PRIVILEGE MANAGEMENT SYSTEM")
	print("=" * 50)
	print("1. Load users from CSV")
	print("2. Create new admin from user")
	print("3. View admin information")
	print("4. View admin privileges")
	print("5. Add a privilege")
	print("6. Remove a privilege")
	print("7. Replace all privileges")
	print("8. Add user to CSV")
	print("9. Remove user from CSV")
	print("10. Exit (or press 'q')")
	print("=" * 50)


def add_user_to_csv(user):
	"""Append a `User` to the CSV file at `csv_path`."""
	file_exists = os.path.isfile(csv_path)
	with open(csv_path, mode='a', newline='', encoding='utf-8') as f:
		fieldnames = ['first_name', 'last_name', 'email', 'age', 'location']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		if not file_exists:
			writer.writeheader()
		writer.writerow({
			'first_name': user.first_name,
			'last_name': user.last_name,
			'email': user.email,
			'age': user.age if user.age is not None else '',
			'location': user.location,
		})
	return True


def load_users_from_csv(users, display=True):
	"""Load users from `csv_path` into the provided `users` list.

	If `display` is True the users are printed. Returns number of users loaded.
	"""
	users.clear()
	if not os.path.isfile(csv_path):
		if display:
			print(f"CSV file not found at {csv_path}")
		return 0
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
	count = len(users)
	if display:
		print(f"Loaded {count} user(s) from CSV")
		for i, u in enumerate(users, 1):
			print(f"{i}. {u.first_name} {u.last_name}")
	return count


def remove_user_from_csv(index):
	"""Remove a user by index (0-based) from the CSV and rewrite the file."""
	if not os.path.isfile(csv_path):
		print("CSV not found; nothing to remove.")
		return False
	with open(csv_path, mode='r', newline='', encoding='utf-8') as f:
		rows = list(csv.DictReader(f))
	if not (0 <= index < len(rows)):
		print("Index out of range; no changes made.")
		return False
	# remove selected row
	removed = rows.pop(index)
	with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
		fieldnames = ['first_name', 'last_name', 'email', 'age', 'location']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for row in rows:
			writer.writerow(row)
	return True


def view_user_details(users):
	"""Display detailed information for loaded users.

	If no users are loaded, prompts to load them first.
	"""
	if not users:
		print("No users loaded. Load users first (option 1).")
		return

	print("\nUser Details:")
	for i, u in enumerate(users, 1):
		print(f"{i}. {u.first_name} {u.last_name}")
		if u.age is not None:
			print(f"   Age: {u.age}")
		if u.email:
			print(f"   Email: {u.email}")
		if u.location:
			print(f"   Location: {u.location}")
	print()



def get_or_create_alexander_admin(users, existing_admin=None):
	"""Return an Admin instance for Alexander.

	Searches loaded `users` for a user whose first name equals 'alexander' (case-insensitive).
	If found, returns an Admin based on that user. If an `existing_admin` is provided
	it is returned to preserve in-session privilege changes.
	If not found, creates a new Admin named 'Alexander Admin' with `DEFAULT_PRIVILEGES`.
	"""
	if existing_admin is not None:
		return existing_admin
	# Try to find Alexander in loaded users
	for u in users:
		if u.first_name and u.first_name.strip().lower() == 'alexander':
			admin = Admin(u.first_name, u.last_name, email=u.email, age=u.age, location=u.location)
			admin.set_privileges(list(DEFAULT_PRIVILEGES))
			return admin
	# Not found — create a default Alexander admin
	return Admin('Alexander', 'Admin', email='', age=None, location='', privileges=list(DEFAULT_PRIVILEGES))


def interactive_mode(users):
	"""Interactive mode to manage admin and privileges."""
	alex_admin = None

	while True:
		display_menu()
		choice = input("Enter your choice (1-10 or q): ").strip().lower()
		
		if choice == "1":
			# View users from CSV (loads and displays)
			load_users_from_csv(users, display=True)
			# Offer to view full details of loaded users
			view_choice = input("Press 'v' to view details of loaded users, or press Enter to continue: ").strip().lower()
			if view_choice == 'v':
				view_user_details(users)
		
		elif choice == "2":
			if not users:
				print("No users available. Load users first (option 1).")
				continue
			
			print("\nAvailable users:")
			for i, u in enumerate(users, 1):
				print(f"{i}. {u.first_name} {u.last_name}")
			
			try:
				user_idx = int(input("Select user number: ")) - 1
				if 0 <= user_idx < len(users):
					selected_user = users[user_idx]
					admin = Admin(
						selected_user.first_name,
						selected_user.last_name,
						email=selected_user.email,
						age=selected_user.age,
						location=selected_user.location
					)
					print(f"\nAdmin created: {admin.first_name} {admin.last_name}")
				else:
					print("Invalid user number")
			except ValueError:
				print("Invalid input")
		
		elif choice == "3":
			# View admin information — only Alexander is treated as the admin here
			alex_admin = get_or_create_alexander_admin(users, existing_admin=alex_admin)
			print()
			alex_admin.describe_user()
			alex_admin.greet_user()
			# Always show Alexander's privileges when viewing admin info
			alex_admin.show_privileges()
		
		elif choice == "4":
			alex_admin = get_or_create_alexander_admin(users, existing_admin=alex_admin)
			alex_admin.show_privileges()
		
		elif choice == "5":
			# Add a privilege to Alexander (admin)
			alex_admin = get_or_create_alexander_admin(users, existing_admin=alex_admin)
			privilege = input("Enter privilege to add: ").strip()
			if privilege:
				current = alex_admin.get_privileges()
				current.append(privilege)
				alex_admin.set_privileges(current)
				print(f"Privilege '{privilege}' added successfully!")
				alex_admin.show_privileges()
			else:
				print("Privilege cannot be empty")
		
		elif choice == "6":
			# Remove a privilege from Alexander (admin)
			alex_admin = get_or_create_alexander_admin(users, existing_admin=alex_admin)
			current = alex_admin.get_privileges()
			if not current:
				print("No privileges to remove")
			else:
				print("\nCurrent privileges:")
				for i, priv in enumerate(current, 1):
					print(f"{i}. {priv}")
				try:
					priv_idx = int(input("Select privilege number to remove: ")) - 1
					if 0 <= priv_idx < len(current):
						removed = current.pop(priv_idx)
						alex_admin.set_privileges(current)
						print(f"Privilege '{removed}' removed successfully!")
						alex_admin.show_privileges()
					else:
						print("Invalid privilege number")
				except ValueError:
					print("Invalid input")
		
		elif choice == "7":
			# Replace all privileges for Alexander (admin)
			alex_admin = get_or_create_alexander_admin(users, existing_admin=alex_admin)
			print("Enter new privileges (comma-separated):")
			privileges_input = input("Privileges: ").strip()
			if privileges_input:
				new_privileges = [p.strip() for p in privileges_input.split(',')]
				alex_admin.set_privileges(new_privileges)
				print("Privileges updated successfully!")
				alex_admin.show_privileges()
			else:
				print("No privileges entered")
		
		# (moved exit handling to end) 
		
		elif choice == "8":
			# Add a new user to the CSV
			print("\nEnter new user details to add to CSV:")
			fn = input("First name: ").strip()
			ln = input("Last name: ").strip()
			em = input("Email (optional): ").strip()
			age_input = input("Age (optional): ").strip()
			loc = input("Location (optional): ").strip()
			age_val = None
			if age_input:
				try:
					age_val = int(age_input)
				except ValueError:
					print("Invalid age entered; leaving empty")
			new_user = User(fn, ln, email=em, age=age_val, location=loc)
			add_user_to_csv(new_user)
			print(f"User {fn} {ln} added to CSV")
		
		elif choice == "9":
			# Remove a user from the CSV by listing and selecting
			if not users:
				print("No users loaded. Load users first (option 1).")
				continue
			print("\nLoaded users:")
			for i, u in enumerate(users, 1):
				print(f"{i}. {u.first_name} {u.last_name}")
			try:
				rem_idx = int(input("Select user number to remove from CSV: ")) - 1
				if 0 <= rem_idx < len(users):
					remove_user_from_csv(rem_idx)
					print("User removed from CSV. Reload users to see changes.")
				else:
					print("Invalid user number")
			except ValueError:
				print("Invalid input")
		
		elif choice == "10" or choice == 'q':
			print("Thank you for using the Admin Privilege Management System!")
			break
		else:
			print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
	# Load users from the local users.csv
	users = []
	# Initial load (display existing users)
	load_users_from_csv(users, display=True)
	
	# Start interactive mode
	interactive_mode(users)
