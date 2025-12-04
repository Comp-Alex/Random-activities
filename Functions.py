#Balagso, Alexander John C.
#CPE3A
#Functions Implementation

#Exercise 1
print("Summarize the shirt order")
def make_shirt(size, message):
    """Summarize the shirt order."""
    try:
        print("A " + size + "-sized shirt will be printed with the message: '" + message + "'")
    except Exception as e:
        print("Error:", e)

# Call using positional arguments
make_shirt("Medium", "Dota o ako?")

# Call using keyword arguments
make_shirt(size="Large", message="ML o project ko?")


#Exercise 2
print("Make a shirt with default size and message")
def make_shirt(size="Large", message="I love Python"):
    """Make a shirt with default size and message."""
    try:
        print("A " + size + "-sized shirt will be printed with the message: '" + message + "'")
    except Exception as e:
        print("Error:", e)

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="Medium")

# Custom shirt (different message)
make_shirt(size="Small", message="Python is awesome")
    
#Exercise 3
print("Return a dictionary describing a music album")
def make_album(artist, title, tracks=None):
    """Return a dictionary describing a music album."""
    try:
        album = {"artist": artist, "title": title}
        if tracks:
            album["tracks"] = tracks
        return album
    except Exception as e:
        print("Error:", e)

# Three albums
print(make_album("Vaundy", "Odoroki"))
print(make_album("Coldplay", "yellow"))
print(make_album("Laufey", "Bewitched", tracks=10))

#Exercise 4 (User Albums)
try:
    while True:
        print("\nCreate an album")
        print("Enter album details (or type 'quit' to stop):")
        artist = input("Artist: ")
        if artist.lower() == "quit":
            break
        title = input("Album Title: ")
        if title.lower() == "quit":
            break

        # optional tracks field
        tracks_input = input("Number of tracks (press Enter to skip): ").strip()
        if tracks_input.lower() == "quit":
            print("End album creation.")
            break
        tracks = None
        if tracks_input:
            try:
                tracks = int(tracks_input)
            except ValueError:
                print("Invalid number of tracks; skipping tracks field.")

        album = make_album(artist, title, tracks=tracks)
        print("Album created:", album)
except Exception as e:
    print("Error:", e)
    
#Exercise 5
print("Magicians:")
def show_magicians(magicians):
    try:
        for magician in magicians:
            print(magician)
    except Exception as e:
        print("Error:", e)

magicians = ["My friend's dad", "David Blaine", "Criss Angel"]
show_magicians(magicians)


#Exercise 6
print("The Great Magicians:")
def make_great(magicians):
    try:
        return ["The Great " + magician for magician in magicians]
    except Exception as e:
        print("Error:", e)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ["My friend's dad", "David Blaine", "Criss Angel"]
great_magicians = make_great(magicians)
show_magicians(great_magicians)

#Exercise 7
print("Make sandwitch")
def make_sandwich(*items):
    try:
        print("Making a sandwich with the following items:")
        for item in items:
            print("- " + item)
        print()
    except Exception as e:
        print("Error:", e)

# Three calls with different arguments
make_sandwich("Ham", "Cheese")
make_sandwich("Turkey", "Lettuce", "Tomato", "Mayo")
make_sandwich("Bacon", "Egg", "Avocado", "Spinach", "Cheddar")