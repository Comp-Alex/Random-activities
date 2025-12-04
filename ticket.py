print("\nMovie Tickets Program - Version 2 (Active Variable)")
tickets_sold = 0
print(str(tickets_sold) + " tickets are sold.")
while tickets_sold < 5:  # Limit to 5 tickets
    try:
        age = int(input("Enter your age: "))
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs 10 Pesos.")
        else:
            print("Your ticket costs 15 Pesos.")
        tickets_sold += 1
        print({tickets_sold} + "tickets are sold.")
    except ValueError:
        print("Please enter a valid age.")

print("\nSORRY, ALL TICKETS ARE SOLD OUT!")