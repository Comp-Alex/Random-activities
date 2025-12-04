def main():
    print("Basic Calculator In Python")
    print("Basic operation:")
    print("Addition")
    print("Subtraction") 
    print("Multiplication")
    print("Division")

    while True:
        try:
            A = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            B = float(input("Enter second number: "))
            
            if operation == '+':
                print(A, "+", B, "=", A + B)
            elif operation == '-':
                print(A, "-", B, "=", A - B)
            elif operation == '*':
                print(A, "*", B, "=", A * B)
            elif operation == '/':
                if B != 0:
                    print(A, "/", B, "=", A / B)
                else:
                    print("Error: Division by zero!")
            else:
                print("Invalid operation")
                
            again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                print("Thank you for using the calculator!")
                break
                
        except ValueError:
            print("Invalid input! Please enter numeric values.")


    main()