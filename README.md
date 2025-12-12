Task 1:

Inputs

- num1 = int(input("Enter the first number:"))  
  Prompts the user, reads a line of text, and converts it from string to integer before storing it in num1.
- num2 = int(input("Enter the second number:"))  
  Does the same for the second value and stores it in num2.

Operations

Each print statement labels the operation and evaluates an expression using the two integers:

- print("Addition:", num1+num2) uses the + operator to add the numbers.
- print("Subraction:", num1-num2) uses - to subtract num2 from num1.
- print("Multipliction:", num1*num2) uses * to multiply them.
- print("Division:", num1/num2) uses / for floating-point division of num1 by num2.


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
