def count_vowels_consonants(sentence):
    vowels = 0
    consonants = 0
    # Define a set of vowels for efficient lookup
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    # Convert the sentence to lowercase to handle both uppercase and lowercase letters
    sentence = sentence.lower()
    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a letter
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

def main():
    sentence = input("Enter a sentence: ")
    num_vowels, num_consonants = count_vowels_consonants(sentence)
    print("Number of vowels:", num_vowels)
    print("Number of consonants:", num_consonants)

if __name__ == "__main__":
    main()
