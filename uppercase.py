def convert_case(input_string):

lowercase_string = input_string.lower()
    
    return uppercase_string, lowercase_string
input_string = "Hello World"
uppercase_result, lowercase_result = convert_case(input_string)
print("Original String:", input_string)
print("Uppercase String:", uppercase_result)
print("Lowercase String:", lowercase_result)
