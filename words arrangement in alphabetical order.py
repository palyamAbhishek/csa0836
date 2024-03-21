def sort_letters_alphabetically(word):
    # Convert the word to a list of characters
    letters = list(word)
    # Sort the list of characters alphabetically
    letters.sort()
    # Join the sorted characters back into a string
    sorted_word = ''.join(letters)
    return sorted_word

def main():
    word = input("Enter a word: ")
    sorted_word = sort_letters_alphabetically(word)
    print("Word with letters arranged alphabetically:", sorted_word)

if __name__ == "__main__":
    main()
