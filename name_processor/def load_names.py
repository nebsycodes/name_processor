def load_names():
    #load list of names
    names = [
        "Ash Ketchum",
        "Brock",
        "Misty",
    ]
    return names
#FUNCTIONS
def input_names(names):
    print("Enter names (type 'done' when finished):")
    while True:
        name = input("Name: ")
        if name.lower() == 'done':
            break
        names.append(name)
    return names
#sort names
def sort_names(names):
    return sorted(names)

#filter names query
def filter_names (names, query):
    return [name for name in names if query.lower() in name.lower()]

#display names
def display_names(names):
    for name in names:
        print(name)
        
#save names to a file
def save_names_to_file(names, filename):
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + '\n')
            
#load names from the file
def load_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            names = [line.strip() for line in file]
        return names
    except FileNotFoundError:
        print(f"No such file: {filename}")
        
#main screen
def main():
    names = load_names()
    while True:
        print("\nWhat would you like to do?")
        print("1. Input names")
        print("2. Display names")
        print("3. Sort names")
        print("4. Filter names")
        print("5. Save names to new file")
        print("6. Load names from file")
        print("7. Exit")
        choice = input("Choose a number:")
        #choice directory
        if choice == '1':
            names = input_names(names)
        elif choice == '2':
            display_names(names)
        elif choice == '3':
            sorted_names = sort_names(names)
            print("Sorted names completed")
        elif choice == '4':
            query = input("Enter a string to filter names: ")
            filtered_names = filter_names(names, query)
            print("Filtered names completed")
        elif choice == '5':
            filename = input("Enter a filename:")
            save_names_to_file(names, filename)
            print(f"Names saved to {filename}")
        elif choice == '6':
            filename = input("Enter filename to load names: ")
            names = load_names_from_file(filename)
            print(f"Names loaded from {filename}")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again")
            
if __name__ == "__main__":
    main()
    
    