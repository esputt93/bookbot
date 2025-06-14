def get_book_text(file_path):
  with open(file_path) as file:
    file_contents = file.read()
  return file_contents

def main(file):
  book_text = get_book_text(file)
  return book_text

from stats import word_count
from stats import char_count
from stats import char_count_sorted


book_path = "books/frankenstein.txt"
book_content = main(book_path)
words = word_count(book_content)
book_print = char_count(book_content)
letter_list = char_count_sorted(book_print)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {words} total words")
print("--------- Character Count -------")

for i in range(len(letter_list)):
   print(f"{letter_list[i]["char"]}: {letter_list[i]["num"]}")
