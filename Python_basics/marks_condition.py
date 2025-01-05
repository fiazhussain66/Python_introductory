percentage_numb = float(input("The numbers in percentage are: "))

if percentage_numb > 80:
    print("Excellent")
elif percentage_numb > 60:
    print("Good")
elif percentage_numb >= 40:
    print("Average")
else:
    print("Fail")