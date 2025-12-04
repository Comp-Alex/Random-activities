#Exercise 3
print("\nWelcome to the Color Ball Guessing Game!")
ball01 = 'green'
ball02 = 'yellow'
ball03 = 'red'
guess03 = input("Guess the color (red/green/blue/yellow): ").lower()
if guess03 == ball01:
    print("Congratulations! The ball was " + ball01 + ". You earned 5 points!")
elif guess03 == ball02:
    print("Congratulations! The ball was " + ball02 + ". You earned 10 points!")
elif guess03 == ball03:
    print("Congratulations! The ball was " + ball03 + ". You earned 15 points!")