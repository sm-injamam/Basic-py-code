
a = [];
x, y = 0, 0
line = input("Give your value here: \n")
while line:
    a.append(line)
    line = input()
# print(a)
for i in a:
    if 'UP' in i:
        y += int(i[-1])
    elif 'DOWN' in i:
        y -= int(i[-1])
    elif 'LEFT' in i:
        x -= int(i[-1])
    elif 'RIGHT' in i:
        x += int(i[-1])

print("Output: ","{:.2f}".format((x ** 2 + y ** 2) ** 0.5))