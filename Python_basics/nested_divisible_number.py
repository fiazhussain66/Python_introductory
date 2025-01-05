numb = int(input("Enter the number: "))

if numb % 21 == 0:
    print("The number is divisible by 21.")
else:
    if numb % 7 == 0 or numb % 3 ==0:
        print("The number is not divisble by 21 but divisible by 7  or 3.")
    else:
        print("The number is not divisible by 21 and neither divisible by 7 and 3.")