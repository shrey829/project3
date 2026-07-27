print("Welcome to Pattern Generator and Number Analyzer!")
print("1 for generating a pattern")
print("2 for generating a range of numbers")
print("3 Exit")

num = int(input("Enter your choice: "))
sum = 0

match num:
    case 1:
        print("Rows value should be positive.")
        rows = int(input("Enter the number of rows: "))

        if rows > 0:
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()
        else:
            pass

    case 2:
        print("Start of range should be less than end of range.")
        num1 = int(input("Enter the starting number: "))
        num2 = int(input("Enter the ending number: "))

        if num2 > num1:
            for i in range(num1, num2 + 1):
                if i % 2 == 0:
                    print(f"Number {i} is even")
                else:
                    print(f"Number {i} is odd")

                sum += i

            print("Sum is:", sum)
        else:
            pass

    case 3:
        print("Thank you! Exiting the program... Goodbye!")
        exit()

    case _:
        print("Invalid choice")
