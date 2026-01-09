def factorial(num):
    n=num
    fact=1
    while(n>0):
        fact=fact*n
        n-=1
    print(f"Factorial of {num}={fact}")
num=int(input("Enter a number:"))
factorial(num)
