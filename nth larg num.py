def nth_largest(arr, n):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the nth largest element
    return arr[n - 1]

# Example usage:
arr = [5, 10, 2, 8, 15]
n = 2
print("The 4th largest number in the array is: {nth_largest(arr, n)}")
