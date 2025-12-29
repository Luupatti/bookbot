from stats import number_of_words, number_of_characters, book_report
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():


    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

    book = get_book_text(sys.argv[1])
    number = number_of_words(book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print("Found", number, "total words")
    print("--------- Character Count -------")
    characters = number_of_characters(book)
    book_report(characters)
    print("============= END ===============")
main()

