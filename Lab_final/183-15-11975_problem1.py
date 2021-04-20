n=int(input("Enter your Number: " ))
sum = 0
for i in range(1, n+1):
    if i % 2 == 1:
        sum += i / (i + 1) ** 2
    else:
        sum += i ** 2 / (i + 1)

print("Output: ","{:.2f}".format(sum))