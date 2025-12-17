Task 2:

Inputs

- first_name = str(input("Enter your first name:"))  
  Prompts the user, reads text from the keyboard, and ensures it is stored as a string in first_name.
- last_name = str(input("Enter your last name:"))  
  Prompts similarly for the last name and stores it in last_name.

String building and output

- fullname = first_name + last_name  
  Concatenates the two strings into one; if you want a space, you would use first_name + " " + last_name.
- print(f"Hello, {fullname}! Welcome to the Python program.")  
  Uses an f-string to embed the fullname variable directly inside the output message and prints the final greeting to the console.
