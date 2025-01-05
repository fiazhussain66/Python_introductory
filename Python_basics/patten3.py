numb = int(input("ENter the number: "))

for i in range(1, numb+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()
    
    
for i in range(1, numb+1):
    for j in range(1, i+1):
        print(chr(j+64), end = "")
    print()