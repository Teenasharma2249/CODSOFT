# Pyhton program to make a simple calculator

def add(num1, num2):   #to add
    return num1 + num2

def subtract(num1, num2): # to subtract
    return num1 - num2

def multiply(num1, num2):  # to multiply 
    return num1 * num2

def divide(num1, num2): # to divide
    return num1 / num2

print("Select operation.\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide ")

while True:
   
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        
       