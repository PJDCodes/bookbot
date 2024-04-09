def word_count(words):
    # prints the number of words in the book
    print(len(words.split()))

def letter_count(input_str):
    # prints a dictionary of unique characters and the number of times they occur in the book
    lowered_string = input_str.lower()
    letter_dict = {}    
    for letters in lowered_string:
        if letters in letter_dict:
            letter_dict[letters] += 1
        else:
            letter_dict[letters] = 1
    print(letter_dict)
         
def main():

    with open("books/frankenstein.txt") as f:
        # reads the contents of the text file and prints to console
        file_contents = f.read()
        print(file_contents)
    word_count(file_contents)
    letter_count(file_contents)

if __name__ == "__main__":
    main()


    