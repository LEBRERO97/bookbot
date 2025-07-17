def get_book_content(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
    return content

def get_num_words(path_to_file):
    content = get_book_content(path_to_file)
    word_list = content.split()
    num_words = len(word_list)
    return num_words

def get_num_char(path_to_file):
    content = get_book_content(path_to_file)
    content_lwr = content.lower()
    word_list = content_lwr.split()
    char_dict = {}
    for word in word_list:
        for char in word:
            if char in char_dict:
                char_dict[char] = char_dict[char] + 1
                
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items[1]

def dict_sort(dictionary):
    return sorted(dictionary.items(), key=sort_on, reverse=True)