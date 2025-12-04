#Balagso, Alexander John C.
#CPE3A
#Dictionary Implementation

#Exercise 1
print("Person Dictionary\n")
try:
    person = {
        "first_name": "Alexander John",
        "last_name": "Balagso",
        "age": 20,
        "city": "Batangas"
    }

    # Print each piece of information
    print("First Name:", person["first_name"])
    print("Last Name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])

except Exception as e:
    print("An error occurred:", e)

# Exercise 2
print("\nFavorite Numbers Dictionary\n")
try:
    favorite_numbers = {
        "Anne": 7,
        "Abi": 12,
        "Mylene": 3,
        "Ella": 9,
        "Samantha": 21
    }

    # Let the user enter a number and show who has that favorite number
    while True:
        user_input = input("Enter a number to find whose favorite it is (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("\nAvailable Favorite numbers in dictionary")
            for name, number in favorite_numbers.items():
                print(name + "'s favorite number is " + str(number))
            break
        try:
            num = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")
            continue

        matches = [name for name, val in favorite_numbers.items() if val == num]
        if matches:
            if len(matches) == 1:
                print(matches[0] + "'s favorite number is " + str(num) + ".")
            else:
                print(", ".join(matches) + " have " + str(num) + " as their favorite number.")
        else:
            print("Not available in the dictionary.")
except Exception as e:
    print("An error occurred:", e)

#Exercise 3
print("\nRivers and Countries Dictionary\n")
try:
    rivers = {
        "nile": "egypt",
        "amazon": "brazil",
        "yangtze": "china"
    }

    # Sentence about each river
    for river, country in rivers.items():
        print("The " + river.title() + " runs through " + country.title() + ".")

    print("\nRivers included in the dictionary:")
    for river in rivers.keys():
        print(river.title())

    print("\nCountries included in the dictionary:")
    for country in rivers.values():
        print(country.title())

except Exception as e:
    print("An error occurred:", e)