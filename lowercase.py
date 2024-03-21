def convert_case(input_string):
    # Convert to uppercase
    uppercase_string = input_string.upper()
    
    # Convert to lowercase
    lowercase_string = input_string.lower()
    
    return uppercase_string, lowercase_string

# Test the function
input_string = "Hello World"
uppercase_result, lowercase_result = convert_case(input_string)
print("Original String:", input_string)
print("Uppercase String:", uppercase_result)
print("Lowercase String:", lowercase_result)
