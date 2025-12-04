#Balagso, Alexander John C.
#CPE3A
#Tuples

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

buffet_foods = ("burger", "steak", "salad", "pasta", "ice cream")
print("\nRevised buffet menu:")
for food in buffet_foods:
	print(food)

#Exercise 2 - your own list
print("\nExercise 2 - Your Own List Program Version 2")
movies = ["The Star wars", "Maze Runner", "Interstellar", "The Martian", "Hello World"]

print("The movie " + movies[0] + " is the first movie I've watched!")
print("I really love the movie " + movies[1] + "!")
print("The movie " + movies[2] + " is the most beautiful movie I've seen.")
print("The flow of " + movies[3] + " is amazing! This is a great movie.")
print("This " + movies[4] + " movie is an actual movie.")

#exercise 3 - Seeing the world
print('Exercise 3 - Seeing the World Program')
places = ("Japan", "Indonesia", "Italy", "France", "Germany")

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
    
# Exercise 4 - Every function
print('\nExercise 4 - Every Function Program')
print('\nTopic: Demonstrate common list operations and show list state after each operation')

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

#Exercise 5 - Lomi
print('\nExercise 5 - Lomi Program')
Kinds_of_lomi = ('chicken Lomi', 'pork Lomi', 'Special Lomi', 'Regular Lomi', 'Mega Lomi')
for lomi in Kinds_of_lomi:
    print("I like to eat " + lomi + ".")
print("\nI really really love " + Kinds_of_lomi[0] + "!")
print("I really really love " + Kinds_of_lomi[1] + "!")
print("I really really love " + Kinds_of_lomi[2] + "!")

#Exercise 6 - Cubes
print('\nExercise 6 - Cubes Program')

cubes = [number**3 for number in range(1, 11)]

# Print each cube using a for loop
for cube in cubes:
    print(cube)