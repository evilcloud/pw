#!/usr/local/bin/python3

import pyperclip
import sys
import string
from random import choice

pass_lenght = 40


try:
    pass_input = sys.argv[1]
    pass_lenght = int(pass_input)
except IndexError:
    print(f"No args — generating {pass_lenght} char long pass")
except ValueError:
    print(f"{pass_input} is not a natural number. Using default settings")
except Exception as e:
    print(f"Error: ", e)

password = ""
char_punct = list(string.punctuation)
char_digits = list(string.digits)
char_ascii = list(string.ascii_letters)

for i in range(pass_lenght):
    password += choice([choice(char_ascii), choice(char_digits), choice(char_punct)])

pyperclip.copy(password)
print(f"Pass of {len(pyperclip.paste())} chars copied in the clipboard")
print(f"\n\n{pyperclip.paste()}\n")
