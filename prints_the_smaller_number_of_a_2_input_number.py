number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if number1 < number2:
    print(f"Number {number1} is smaller")
elif number2 < number1:
    print(f"Number {number2} is smaller")
else:
    print("The number are the same")