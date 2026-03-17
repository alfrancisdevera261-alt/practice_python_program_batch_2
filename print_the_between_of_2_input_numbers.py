number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if number1 < number2:
    for i in range(number1, number2-1):
        print(i+1)
else:
    for i in range(number2, number1-1):
        print(i+1)