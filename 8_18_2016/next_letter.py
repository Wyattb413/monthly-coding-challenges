'''
Write a function that changes every letter in a string to the next letter
in the alphabet. Capital letters must remain capitalized.abs
'''

import sys

words = sys.argv[1:]


def next_letter(words):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                'w', 'x', 'y', 'z']
    new_letters = []
    new_string = ''

    for word in words:
        for letter in word:
            capitalize = False

            if letter.isupper():
                capitalize = True

            letter = letter.lower()

            try:
                if letter == 'z':
                    index = alphabet.index('a')
                else:
                    index = (alphabet.index(letter) + 1)

                if capitalize:
                    new_letters.append(alphabet[index].capitalize())
                else:
                    new_letters.append(alphabet[index])
            except:
                new_letters.append(letter)

        new_letters.append(' ')

    return(new_string.join(new_letters))

print(next_letter(words))
