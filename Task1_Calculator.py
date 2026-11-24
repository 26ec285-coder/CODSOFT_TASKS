
def calculator():
    while True:
        print("\n========== CALCULATOR ==========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Thank you for using Calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                operator = "+"

            elif choice == "2":
                result = num1 - num2
                operator = "-"

            elif choice == "3":
                result = num1 * num2
                operator = "*"

            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operator = "/"

            elif choice == "5":
                if num2 == 0:
                    print("Error: Modulus by zero is not allowed.")
                    continue
                result = num1 % num2
                operator = "%"

            print(f"Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("Please enter valid numbers.")


calculator()
