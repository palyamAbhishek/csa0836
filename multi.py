# Get input from the user
number = int(input("Enter a number: "))

# Display the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
