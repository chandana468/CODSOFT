def calculator():
    while True:
        print("\nSimple Calculator")
        print("Operations: +, -, *, /")
        print("Enter 'exit' to stop.")

        # Taking user input
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        num2 = input("Enter second number: ")
        if num2.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        operation = input("Enter operation (+, -, *, /): ")
        if operation.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        # Validating inputs
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
            continue

        # Performing calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Error: Invalid operation. Please enter +, -, *, or /.")
            continue

        # Display result
        print(f"Result: {result}")

# Run the calculator
calculator()