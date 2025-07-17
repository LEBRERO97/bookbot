import sys
from stats import get_num_words, get_num_char, dict_sort

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def main():
    num_words = get_num_words(sys.argv[1])
    char_dict = get_num_char(sys.argv[1])
    sorted_list = dict_sort(char_dict)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for lst in sorted_list:
        if lst[0].isalpha():
            print(f'{lst[0]}: {lst[1]}')
    print('============= END ===============')
        

main()