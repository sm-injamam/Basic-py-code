value = int(input('input your number:'))
sum = 0
for digit in str(value):
    sum = sum + int(digit)

    if (sum % 2 == 0):
        parity = 'Even'

else:
    Parity = 'Odd'

if ((value % 2 == 0) and (sum % 2 == 0)):
    Result = 'True'
if (value % 2 != 0 and sum % 2 != 0):
    Result = 'True'


else:
    Result = 'False'
print('sum:', sum, ' parity: ', Parity, 'Result:', Result)