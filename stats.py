def word_count(book_text):
  word_list = book_text.split()
  return len(word_list)

def char_count(book_text):
  lower_case = book_text.lower()
  letter_count = {}
  for letter in lower_case:
    if letter in letter_count:
      letter_count[letter] += 1   
    else:
      letter_count[letter] = 1
  return letter_count
  
def sort_on(dict):
  return dict["num"]

def char_count_sorted(dict):
  initial_list = []
  for key in dict:
    if key.isalpha() == True:
      new_dict = {
        "char": key,  "num": dict[key]
      }
      initial_list.append(new_dict)   
  initial_list.sort(reverse=True, key=sort_on)
  return initial_list
    
  
    

