try:
    with open("new_file.txt", "x") as f:
        f.write("This only works if 'new_file.txt' does not exist yet.")
except FileExistsError:
    print("Error: The file already exists.")
    
    
    