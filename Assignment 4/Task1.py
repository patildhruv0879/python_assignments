try:
        file= open("Sample.txt", 'r')
        for line in file:
            print(line.strip())
        file.close()
        print("File read successfully.")
except FileNotFoundError:
    print("Error: 'Sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")