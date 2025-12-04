# Exercise 1: Car Rental
print("\n--- Exercise 1: Car Rental ---")
car_type = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car_type}.")

# Exercise 2: Restaurant Seating
print("\n--- Exercise 2: Restaurant Seating ---")
group_size = int(input("How many people are in your group? "))
if group_size > 10:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")

# Exercise 3: Multiples of Ten
print("\n--- Exercise 3: Multiples of Ten ---")
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

# Exercise 4 is same as Exercise 2, so skipping...

# Exercise 5: Pizza Toppings (using while loop)
print("\n--- Exercise 5: Pizza Toppings (While Loop) ---")
topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() != 'quit':
        print(f"I'll add {topping} to your pizza.")

# Exercise 5: Pizza Toppings (using for loop with break)
print("\n--- Exercise 5: Pizza Toppings (For Loop) ---")
for i in range(100):  # Large range, will break when user enters 'quit'
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")

# Exercise 6: Movie Tickets
print("\n--- Exercise 6: Movie Tickets ---")
while True:
    age = input("Enter your age (or 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs 10 Pesos.")
    else:
        print("Your ticket costs 15 Pesos.")

# Exercise 7: Three Exits
print("\n--- Exercise 7: Three Exits ---")

# Version 1: Conditional test in while statement
print("\nVersion 1 - Conditional test:")
active = True
age = ""
while active:
    age = input("Enter your age (or 'quit' to exit): ")
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs 10 Pesos.")
        else:
            print("Your ticket costs 15 Pesos.")

# Version 2: Active variable
print("\nVersion 2 - Active variable:")
max_tickets = 3
tickets_sold = 0
while tickets_sold < max_tickets:
    age = int(input(f"Enter age for ticket {tickets_sold + 1}: "))
    tickets_sold += 1
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs 10 Pesos.")
    else:
        print("Your ticket costs 15 Pesos.")

# Version 3: Break statement
print("\nVersion 3 - Break statement:")
while True:
    age = input("Enter your age (or 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs 10 Pesos.")
    else:
        print("Your ticket costs 15 Pesos.")

# Exercise 8: Infinity
print("\n--- Exercise 8: Infinity ---")
print("Press CTRL+C to stop the infinite loop")
while True:
    print("This is an infinite loop!")