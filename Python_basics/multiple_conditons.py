phy_marks = float(input("Enter the marks of obtained in physics: "))
math_marks = float(input("Enter the marks of obtained in math: "))

if phy_marks > 80 and math_marks > 80:
    print("A-Grade")
elif phy_marks > 80 or math_marks > 80:
    print("B-Grade")
else:
    print("C-Grade")