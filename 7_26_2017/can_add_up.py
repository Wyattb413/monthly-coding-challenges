import sys

'''
Grabs first argument passed (assumed to be list),
strips [],
splits to create array of int
'''
list_of_numbers = map(int, sys.argv[1].strip('[]').split(','))

if len(list_of_numbers) <= 1:
    raise ValueError('Please provide a list with two or more integers, thank you :)')

integer = int(sys.argv[2])

def get_numbers(list_of_numbers, integer):
    for (i, num) in enumerate(list_of_numbers):
        for j in list_of_numbers[i + 1:-1]:
            if num + j == integer:
                return('I found the numbers, [{},{}], in the list you provided to equal your integer, {}'.format(num, j, integer))

print(get_numbers(list_of_numbers, integer))