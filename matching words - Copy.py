def count_matching_characters(str1, str2):
    # Initialize a counter for matching characters
    match_count = 0
    # Ensure both strings have the same length
    if len(str1) != len(str2):
        return "The strings must have the same length"
    # Iterate through the characters of the strings
    for i in range(len(str1)):
        # Check if the characters at the same index match
        if str1[i] == str2[i]:
            match_count += 1
    return match_count

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    num_matches = count_matching_characters(string1, string2)
    if isinstance(num_matches, int):
        print("Number of matching characters at the same index:", num_matches)
    else:
        print(num_matches)

if __name__ == "__main__":
    main()
