import sys
from stats import (
  word_count,
  char_count,
  char_count_sorted
)


def get_book_text(file_path):
  with open(file_path) as file:
    file_contents = file.read()
  return file_contents

def main():
  book_path = ""
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_path = sys.argv[1]
  text = get_book_text(book_path)
  num_words = word_count(text)
  num_chars_dict = char_count(text)
  chars_sorted_list = char_count_sorted(num_chars_dict)
  print_report(book_path, num_words, chars_sorted_list)

def print_report(book_path, num_words, chars_sorted_list_):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for i in range(len(chars_sorted_list_)):
    print(f"{chars_sorted_list_[i]['char']}: {chars_sorted_list_[i]['num']}")
  print("============= END ===============")

main()

