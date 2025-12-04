#Balagso, Alexander john C.
#CPE3A
#Exceptions

# Exercise 1 - CH01 – CH03: Apply the try-catch Exception to the exercises 
print("Chapter 1 - Student Information")
name = 'Alexander John C. Balagso'
address = 'MUNTING-PULO LIPA CITY, BATANGAS'
YearCourse = 'CPE3A'
try:
    print('Student name: ' + name)
    print('Address: ' + address)
    print('Year and Course: ' + YearCourse)
except Exception as e:
    print('Error: ' + str(e))

print("\nChapter 2 - Varirables and strings")
try:
    #2-1
    print("Exercise 2-1")
    A = "William"
    print("Pakopya Assignment", A)
    #2-2
    print("exercise 2-2")
    B = "Marc"
    print("Original name: " + B)
    print("Lowercase: " + B.lower())
    print("Uppercase: " + B.upper())
    print("Title case: " + B.title())
    #2-3
    print("Exercise 2-3")
    C = 'Socrates once said,"The only true wisdom is in knowing you know nothing."'
    print(C)
    #2-4
    print("Exercise 2-4")
    famous_person = "Socrates"
    message = 'The only true wisdom is in knowing you know nothing.'
    print(famous_person + ' once said, "' + message + '"')
    #2-5
    print("Exercise 2-5")
    print("Addition: 5 + 3 =", 5 + 3)
    print("Subtraction: 11 - 3 =", 11 - 3) 
    print("Multiplication: 4 * 2 =", 4 * 2)
    print("Division: 16 / 2 =", 16 / 2)
    #2-6
    print("Exercise 2-6")
    Masarap_na_number = 69
    print("My favorite number is " + str(Masarap_na_number))
except Exception as e:
    print('Error: ' + str(e))

#Exercise 2 - CH04 – CH07: Apply the try-catch-finally Exception to the exercises
print("\nChapter 3&4 - Fundamentals and If Statements")
#Exercise 1
try:
    print("Welcome to the Color Ball Guessing Game!")
    ball_color = 'green'
    guess01 = input("Guess the color (red/green/blue/yellow): ").lower()
    if guess01 == ball_color:
        print("Congratulations! The ball was %s. You earned 5 points!" % ball_color)
    else:
        print("Sorry, the ball was %s. Try again!" % ball_color)
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 1.")
#Exercise 2
try:
    print("\nWelcome to the Color Ball Guessing Game!")
    ballgreen = 'green'
    guess02 = input("Guess the color (red/green/blue/yellow): ").lower()
    if guess02 == ballgreen:
        print("Congratulations! The ball was %s. You earned 5 points!" % ballgreen)
    else:
        print("Congratulations! you just earned 10 points!")
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 2.")
    
#Exercise 3
try:
    print("\nWelcome to the Color Ball Guessing Game!")
    ball01 = 'green'
    ball02 = 'yellow'
    ball03 = 'red'
    guess03 = input("Guess the color (red/green/blue/yellow): ").lower()
    if guess03 == ball01:
        print("Congratulations! The ball was %s. You earned 5 points!" % ball01)
    elif guess03 == ball02:
        print("Congratulations! The ball was %s. You earned 10 points!" % ball02)
    elif guess03 == ball03:
        print("Congratulations! The ball was %s. You earned 15 points!" % ball03)
    else:
        print("Sorry, that color wasn't one of the balls. Try again!")
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 3.")
    
#Exercise 4
print("\nStages of Life Program")
try:
    age = int(input("Enter a person's age: "))
    if age < 2:
        print("This person is a baby.")
    elif age < 4:
        print("This person is a toddler.")
    elif age < 13:
        print("This person is a kid.")
    elif age < 20:
        print("This person is a teenager.")
    elif age < 65:
        print("This person is an adult.")
    else:
        print("This person is an elder.")
except ValueError:
    print("Please enter a valid number for age.")
finally:
    print("End of Exercise 4.")

print("\nChapter 5 Loops")
#Exercise 1 - Car Rental
print("Car Rental Program")
try:
    car_type = input("What kind of rental car would you like? ")
    print("Let me see if I can find you a " + car_type + ".")
except Exception as e:
    print("An error occurred while getting your car preference:", str(e))
finally:
    print("End of Exercise 1.")
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
finally:
    print("End of Exercise 2.")
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
finally:
    print("End of Exercise 3.")
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
finally:
    print("End of Exercise 4.")
#Exercise 5 - Pizza Toppings
print("\nPizza Toppings Program")
try:
    while True:
        topping = input("Enter a pizza topping (or 'quit' to finish): ")
        if topping.lower() == 'quit':
            break
        print("I'll add " + topping + " to your pizza.")
finally:
    print("End of Exercise 5.")
#Exercise 6 - Movie Tickets
print("\nMovie Tickets Program")
while True:
    age_input = input("Enter your age: ")
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
    finally:
        print("End of Exercise 6.")
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
        finally:
            print("End of Version 1.")
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
    finally:
        print("End of Version 2.")
print("\nSORRY, ALL TICKETS ARE SOLD OUT!")
#Exercise 8 - Infinity
print("\nInfinity Loop Program")
try:
    while True:
        print("This is an infinite loop!")
except KeyboardInterrupt:
    print("Loop interrupted by user.")
finally:
    print("End of Exercise 8.")
    
print("\nChapter 6 - Lists")
#Exxercise 1 - Names
try:
    print("Exercise 1 - Names Program")
    names = ["Myke", "Guian", "Charles", "Derrick", "Marc", "William"]
    print(names[0])
    print(names[1])
    print(names[2])
    print(names[3])
    print(names[4])
    print(names[5])
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 1.")
    
#Exercise 2 - Greetings
try:
    print("Exercise 2 - Greetings Program")
    names = ["Myke", "Guian", "Charles", "Derrick", "Marc", "William"]

    print("Boss, " + names[0] + "! May code kana sa python?")
    print("Boss, " + names[1] + "! May code kana sa python?")
    print("Boss, " + names[2] + "! May code kana sa python?")
    print("Boss, " + names[3] + "! May code kana sa python?")
    print("Boss, " + names[4] + "! May code kana sa python?")
    print("Boss, " + names[5] + "! May code kana sa python?")
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 2.")
    
#Exercise 3 - Your Own List Movies
print("Exercise 3 - Own List Program Version 1")
try:
    movies = ["The Star wars", "Maze Runner", "Interstellar", "The Martian", "Hello World"]
    genre = 'Sci-Fi'

    print("The movie " + movies[0] + " is the first movie I've watched!")
    print("I really love the movie " + movies[1] + "!")
    print("The movie " + movies[2] + " is the most beautiful movie I've seen.")
    print("The flow of " + movies[3] + " is amazing! This is a great movie.")
    print("This " + movies[4] + " movie is an actual movie.")
    print("All of the movies I've listed are " + genre + " movies.")
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 3.")

print("\nChapter 7 - Tuples")
#Exercise 1 - buffet
print('Exercise 1 - Buffet Program')
buffet_foods = ("pizza", "steak", "salad", "soup", "cake")
print("Original buffet menu:")
for food in buffet_foods:
	print(food)

try:
	buffet_foods[0] = "burger"
except TypeError as e:
	print("Error: " + str(e))
finally:
    print("End of Exercise 1.")
    
buffet_foods = ("burger", "steak", "salad", "pasta", "ice cream")
print("\nRevised buffet menu:")
for food in buffet_foods:
	print(food)

#Exercise 2 - your own list
print("\nExercise 2 - Your Own List Program Version 2")
movies = ["The Star wars", "Maze Runner", "Interstellar", "The Martian", "Hello World"]
try:
    print("The movie " + movies[0] + " is the first movie I've watched!")
    print("I really love the movie " + movies[1] + "!")
    print("The movie " + movies[2] + " is the most beautiful movie I've seen.")
    print("The flow of " + movies[3] + " is amazing! This is a great movie.")
    print("This " + movies[4] + " movie is an actual movie.")
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 2.")

#exercise 3 - Seeing the world
print('Exercise 3 - Seeing the World Program')
places = ("Japan", "Indonesia", "Italy", "France", "Germany")
try:
    print("\nSeeing the world version 1 'Original order' ")
    print("\nSome beautiful places I'd like to visit:")
    for place in places:
        print("I would love to visit " + str(place) + ".")
    print('\nSeeing the world version 2 "Places in Reverse order & Original order" ')
    print("\nSome beautiful places I'd like to visit in reverse order:")
    for place in reversed(places):
        print("I would love to visit " + str(place) + ".")
    print("\nSome beautiful places I'd like to visit in original order again:")
    for place2 in places:
        print("I would love to visit " + str(place2) + ".")
    print('\nSeeing the world version 3 "Using sort" ')
    print("\nAlphabetical order")
    for place in sorted(places):
        print("I would love to visit " + str(place) + ".")
    print('\nReversed Alphabetical order')
    for place in reversed(sorted(places)):
        print("I would love to visit " + str(place) + ".")
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 3.")

# Exercise 4 - Every function
print('\nExercise 4 - Every Function Program')
print('\nTopic: Demonstrate common list operations and show list state after each operation')
try:
    def show(topic, seq):
        print('\n' + topic)
        print('List state:', seq)

    # Start with a representative list
    languages = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
    show('Original list:', languages)

    # Tuple snapshot (immutable)
    language_tuple = tuple(languages)
    show('Tuple (immutable snapshot):', language_tuple)

    # sort() - in-place
    languages.sort()
    show('After sort() (in-place alphabetical):', languages)

    # reverse sort (in-place reverse)
    languages.sort(reverse=True)
    show('After sort(reverse=True):', languages)

    # sorted() - returns new list, original unchanged when using sorted on a fresh list
    unsorted_languages = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
    print('\nUsing sorted() on a fresh list (does not modify original):', sorted(unsorted_languages))

    # slicing examples
    print('\nSlicing examples:')
    print('First 3 languages:', languages[:3])
    print('Last language:', languages[-1])
    print('Every 2nd language:', languages[::2])

    # unpacking without starred assignment 
    first = languages[0]
    second = languages[1]
    others = languages[2:]
    print('\nUnpacking: First: ' + first + '\nSecond: ' + second + '\nOthers: ' + str(others))

    # for-loop and enumerate
    print('\nFor loop:')
    for lang in languages:
        print('Programming Language:', lang)

    print('\nEnumerate:')
    for i, lang in enumerate(languages, 1):
        print(str(i) + '. ' + lang)

    # membership
    print('\nMembership check: Is "Python" in languages?', 'Python' in languages)

    # simple iterable example
    print('\nIterating over string "Code":')
    for ch in 'Code':
        print(ch, end=' ')
    print()

    # map, filter, reduce examples
    lengths = list(map(len, languages))
    print('\nMap (lengths):', lengths)
    long_names = list(filter(lambda x: (len(x) > 3), languages))
    print('Filter (len>3):', long_names)
    from functools import reduce
    longest = reduce(lambda a, b: a if (len(a) > len(b)) else b, languages)
    print('Reduce (longest):', longest)
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 4.")

#Exercise 5 - Lomi
print('\nExercise 5 - Lomi Program')
try:
    Kinds_of_lomi = ('chicken Lomi', 'pork Lomi', 'Special Lomi', 'Regular Lomi', 'Mega Lomi')
    for lomi in Kinds_of_lomi:
        print("I like to eat " + lomi + ".")
    print("\nI really really love " + Kinds_of_lomi[0] + "!")
    print("I really really love " + Kinds_of_lomi[1] + "!")
    print("I really really love " + Kinds_of_lomi[2] + "!")
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 5.")

#Exercise 6 - Cubes
print('\nExercise 6 - Cubes Program')
try:
    cubes = [number**3 for number in range(1, 11)]
    # Print each cube using a for loop
    for cube in cubes:
        print(cube)
except Exception as e:
    print("Error:", str(e))
finally:
    print("End of Exercise 6.")