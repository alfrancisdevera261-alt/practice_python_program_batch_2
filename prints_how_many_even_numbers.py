even_numbers = 0
for i in range(0,10):
    numbers = int(input(f"Enter number {i+1}: "))
    if numbers % 2 == 0:
        even_numbers += 1
print(even_numbers)