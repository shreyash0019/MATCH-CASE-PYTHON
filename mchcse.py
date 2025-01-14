print("\n************ Simple Calculator ************")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo Division")
print("6. Exponentiation")
print("7. Exit")
print("*******************************************")

choice = input("Enter your choice: ")

if choice == '7':
    print("Exiting the calculator. Program execution successful.")
else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    match choice:
        case '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        case '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        case '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        case '4':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case '5':
            result = num1 % num2
            print(f"Result: {num1} % {num2} = {result}")
        case '6':
            result = num1 ** num2
            print(f"Result: {num1} ^ {num2} = {result}")
        case _:
            print("Invalid choice. Please choose a valid option from the menu.")

    print("Program execution successful.")
