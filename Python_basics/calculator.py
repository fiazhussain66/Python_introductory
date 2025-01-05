numb_1 = int(input("Enter the first number: "))
numb_2 = int(input("Enter the second number: "))

operator = input("Enter the operator: ")
match operator:
    case "+":
        print("The sum of two numbers: ", numb_1 + numb_2)
    case "-":
        print("The subtract of two numbers: ", numb_1 - numb_2)
    case "*":
        print("The multiplication of two numbers: ", numb_1 * numb_2)
    case "/":
        print("The division of two numbers: ", numb_1 / numb_2)
    case "_":
        print("Enter the valid operator.")
    