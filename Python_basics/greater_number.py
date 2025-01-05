numb_1 = int(input("Enter the first number: "))
numb_2 = int(input("Enter the second number: "))
numb_3 = int(input("Enter the third number: "))

if numb_1 > numb_2 and numb_1 > numb_3:
    print("The first number is greater.")
elif numb_2 > numb_1 and numb_2 > numb_3:
    print("Second number is greater.")
else:
    print("Third number is greater.")
