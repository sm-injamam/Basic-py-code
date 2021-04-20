n = int(input("Enter number of rows: "))
num1, num2 = 1, 2*n-3
for i in range(n):
    if i==0:
        for j in range(2*n-1):
            print("*", end="")
    else:
        for j in range(2*n):
            if num1==j or num2==j:
                print("*", end="")
            else:
                print(" ", end="")
        num1 += 1
        num2 -= 1
    print()