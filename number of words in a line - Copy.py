def count_words(line):
    # Split the line into words using space as delimiter
    words = line.split()
    # Count the number of words
    num_words = len(words)
    return num_words

def main():
    line = input("Enter a line of text: ")
    word_count = count_words(line)
    print("Number of words in the line:", word_count)

if __name__ == "__main__":
    main()
