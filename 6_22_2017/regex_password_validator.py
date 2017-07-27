'''
Write regex that will validate a given password
to make sure it meets the following criteria:

- At least 8 characters long
- Contains a lowercase letter
- Contains an uppercase letter
- Contains a number
- Contains a special character
'''

import re
import sys

password = str(sys.argv[1])

def validate(password):
    try:
        match_obj = re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()+]+.*)\S{8,}$', password)
        print("You're password: {} is good!").format(match_obj.group())
    except:
        print("You're password: {} is bad!").format(password)


validate(password)
