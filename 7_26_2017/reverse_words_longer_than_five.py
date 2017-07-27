'''
Write a function that takes a string and returns the same 
string with all five or more letter words reversed.
'''

import sys

string = sys.argv[1]

def parse_sentence(string):
    end_result_array = []
    words = string.split()

    for word in words:
        letter_count = int(count_letters(word))

        if letter_count >= 5:
            word = reverse_word(word)
        
        end_result_array.append(word)

        end_result = ' '.join(end_result_array)

    return end_result

def count_letters(word):
    return len(word)

def reverse_word(word):
    return word[::-1]

print(parse_sentence(string))