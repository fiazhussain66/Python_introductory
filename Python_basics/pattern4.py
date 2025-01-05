numb = int(input("ENter the number: "))


for i in range(1, numb+1):
    print(" " *(numb-i), end="")
    
    for j in range(1, 2*i):
        print(j, end="")
    print()