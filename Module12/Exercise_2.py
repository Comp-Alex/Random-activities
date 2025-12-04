import os

# Guest Book Reader
# Reads and displays all entries from the guest_book.csv file

guest_file = os.path.join(os.path.dirname(__file__), "guest_book.csv")

# Check if the file exists
if not os.path.exists(guest_file):
    print("No guest book file found. Run Exercise_1.py first to create entries.")
else:
    # Read and display the guest book
    print("\n=== GUEST BOOK ENTRIES ===\n")
    
    with open(guest_file, 'r') as f:
        lines = f.readlines()
    
    # Display header
    if len(lines) > 0:
        print(lines[0].strip())
        print("-" * 50)
    
    # Display all guest entries
    if len(lines) > 1:
        for line in lines[1:]:
            print(line.strip())
    else:
        print("No guest entries yet.")
    
    print("\n" + "=" * 50)
    print(f"Total guests: {len(lines) - 1}")
