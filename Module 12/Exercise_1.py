from datetime import datetime
import os

# Guest Book Program
# Prompts users for their name and records their visit in a CSV file

guest_file = os.path.join(os.path.dirname(__file__), "guest_book.csv")

# Initialize the CSV file with headers if it doesn't exist
try:
    with open(guest_file, 'r') as f:
        pass
except FileNotFoundError:
    with open(guest_file, 'w') as f:
        f.write("Date,Name\n")

# Main guest book loop
while True:
    name = input("Enter your name (or 'quit' to exit): ")
    
    if name.lower() == 'quit':
        print("Thank you for visiting! Goodbye!")
        break
    
    # Print greeting
    print(f"Hello {name}! Welcome to our guest book.")
    
    # Record visit in CSV file
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(guest_file, 'a') as f:
        f.write(f"{current_date},{name}\n")
    
    print(f"Your visit has been recorded.\n")
