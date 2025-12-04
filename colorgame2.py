#Exercise 2
print("\nWelcome to the Color Ball Guessing Game!")
ballgreen = 'green'
multi_color = ['red', 'green', 'blue', 'yellow']
guess02 = input("Guess the color (red/green/blue/yellow): ").lower()
if guess02 == ballgreen:
    print("Congratulations! The ball was " + ballgreen + ". You earned 5 points!")
else:
    print("Sorry! The ball could have been one of these: " + ", ".join(multi_color))