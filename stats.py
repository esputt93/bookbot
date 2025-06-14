def word_count(book_text):
  word_list = book_text.split()
  num_words = len(word_list)
  
  return num_words

def char_count(book_text):
  lower_case = book_text.lower()
  # print_letter = ""
  letter_count = {}
  # new_string = "".join(process_chars)
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
  
  # for i in range(len(initial_list)):
  #   print(f"{initial_list[i]["char"]}: {initial_list[i]["num"]}")
  # return
  
  return initial_list
    
  
    

