#Balagso, Alexander John C.
#CPE3A
#loops

#Exercise 1 - Car Rental
print("Car Rental Program")
try:
    car_type = input("What kind of rental car would you like? ")
    print("Let me see if I can find you a " + car_type + ".")
except Exception as e:
    print("An error occurred while getting your car preference:", str(e))

#Exercise 2 - Restaurant Seating
print("\nRestaurant Seating Program")
try:
    group_size = int(input("How many people are in your group? "))
    if group_size > 10:
        print("I'm sorry, you'll have to wait for a table.")
    else:
        print("Your table is ready!")
except ValueError:
    print("Please enter a valid number.")

#Exercise 3 - Multiples of Ten
print("\nMultiples of Ten Program")
try:
    number = int(input("Enter a number: "))
    if number % 10 == 0:
        print(str(number) + " is a multiple of 10.")
    else:
        print(str(number) + " is not a multiple of 10.")
except ValueError:
    print("Please enter a valid number.")

#Exercise 4 - Restaurant Seating (Duplicate of Exercise 2)
print("\nRestaurant Seating Program")
try:
    group_size = int(input("How many people are in your group? "))
    if group_size > 10:
        print("I'm sorry, you'll have to wait for a table.")
    else:
        print("Your table is ready!")
except ValueError:
    print("Please enter a valid number.")

#Exercise 5 - Pizza Toppings
print("\nPizza Toppings Program")
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print("I'll add " + topping + " to your pizza.")

#Exercise 6 - Movie Tickets
print("\nMovie Tickets Program")
while True:
    age_input = input("Enter your age (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    try:
        age = int(age_input)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs 10 Pesos.")
        else:
            print("Your ticket costs 15 Pesos.")
    except ValueError:
        print("Please enter a valid age.")

#Exercise 7 - Three Exits (Based on Movie Tickets)
print("\nMovie Tickets Program - Version 1 (Conditional Test)")
active = True
while active:
    age_input = input("Enter your age (or 'quit' to finish): ")
    if age_input.lower() == 'quit':
        active = False
    else:
        try:
            age = int(age_input)
            if age < 3:
                print("Your ticket is free!")
            elif age <= 12:
                print("Your ticket costs 10 Pesos.")
            else:
                print("Your ticket costs 15 Pesos.")
        except ValueError:
            print("Please enter a valid age.")

#Exercise 8 - Infinity
print("\nInfinity Loop Program")
while True:
    print("This is an infinite loop!")