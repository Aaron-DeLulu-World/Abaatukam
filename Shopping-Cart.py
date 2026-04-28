try:
    with open("list.txt", "x") as f:
        f.write("Initial Data Line\n") 
    print("Success: 'list.txt' created.")
    
except FileExistsError:
    print("Status: 'list.txt' already exists. Ready to append.")

while True:
    print("\n--- Student B: Append Menu ---")
    print("1. Add item to list.txt")
    print("2. View current list.txt")
    print("3. Exit")
    
    choice = input("Choose (1-3): ")

    if choice == "1":
        new_entry = input("Enter the data you want to append: ")
        
        with open("list.txt", "a") as file:
            file.write(new_entry + "\n")
            print(f"Success: '{new_entry}' has been added to the log.\n")

    elif choice == "2":
        try:
            with open("list.txt", "r") as file:
                print("\n--- Current list.txt Content ---")
                print(file.read())
        except FileNotFoundError:
            print("Error: list.txt hasn't been created yet. Add an item first!")

    elif choice == "3":
        print("Closing the program... Gear up for the next push, aeronamii!")
        break
        
    else:
        print("Invalid choice, gaw. Try again.")
