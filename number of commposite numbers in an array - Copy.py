# Sample input
array = [16, 18, 27, 16, 23, 21, 19]
# Count the number of composite numbers
count = 0
for num in array:
    if num < 4:
        continue
    for i in range(2, num):
        if num % i == 0:
            count += 1
            break
# Output the result
print("Number of Composite Numbers =", count)

