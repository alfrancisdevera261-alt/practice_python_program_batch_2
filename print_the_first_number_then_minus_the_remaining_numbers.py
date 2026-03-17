number1 = float(input("Enter number 1: "))
number2 = 0
for i in range(0, 9):
    number2 += float(input(f"Enter number {i+2}: "))
print(f"The result is {number1 - number2}")