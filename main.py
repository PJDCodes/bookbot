def read_file_contents(filename):
        with open(filename) as f:        
            return f.read()
        
def word_count(words):
    # prints the number of words 
    total_words = len(words.split())
    return total_words
    

def letter_count(input_str):
    # prints a dictionary of unique letters and the number of times they occur in the book
    lowered_string = input_str.lower()
    letter_dict = {}    
    for letters in lowered_string:
        if letters.isalpha():
            if letters in letter_dict:
                letter_dict[letters] += 1
            else:
                letter_dict[letters] = 1
    return letter_dict

def book_report(letter_dict, total_words):
        #
        letter_items = list(letter_dict.items())
        sorted_letters = sorted(letter_items, key=lambda item: item[1], reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document")
        print("")
        for letter, freq in sorted_letters:
            print(f"The '{letter}' character was found {freq} times")
        print("--- End report ---")

   
        
def main():
    # reads the contents of the text file and prints to console
    file_contents = read_file_contents("books/frankenstein.txt")
    total_words = word_count(file_contents)
    letter_freq_dict = letter_count(file_contents)
    book_report(letter_freq_dict, total_words)
    

if __name__ == "__main__":
    main()


    