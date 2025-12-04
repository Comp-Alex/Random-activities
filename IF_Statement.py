#balagso, Alexander John C.
#CPE3A
#Control Flow: If statements

# Python 2/3 compatibility
try:
    input = raw_input
except NameError:
    pass

#Exercise 1
print("Welcome to the Color Ball Guessing Game!")
ball_color = 'green'
guess01 = input("Guess the color (red/green/blue/yellow): ").lower()
if guess01 == ball_color:
    print("Congratulations! The ball was %s. You earned 5 points!" % ball_color)
else:
    print("Sorry, the ball was %s. Try again!" % ball_color)

#Exercise 2
print("\nWelcome to the Color Ball Guessing Game!")
ballgreen = 'green'
guess02 = input("Guess the color (red/green/blue/yellow): ").lower()
if guess02 == ballgreen:
    print("Congratulations! The ball was %s. You earned 5 points!" % ballgreen)
else:
    print("Congratulations! you just earned 10 points!")

#Exercise 3
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