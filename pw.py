#!/usr/local/bin/python3

import pyperclip
import sys
import string
import colorama
from colorama import Fore, Back, Style
from random import choice


def load_dict(dict_file):
    word_list = list()
    dict_directory = __file__
    dict_full = dict_directory[:-5] + dict_file
    with open(dict_full) as txt:
        for i in txt:
            word_list.append(txt.readline())
    return word_list


def pick_pass(words_list, pass_lenght):
    pass_combo = []
    pass_combo_lenght = 0
    while pass_combo_lenght != pass_lenght:
        pass_combo.append(choice(words_list).capitalize())
        pass_combo_lenght = len("".join(pass_combo))
        if pass_combo_lenght > pass_lenght:
            pass_combo = []
    return pass_combo


dict_name = "1-1000.txt"
chars_numbers = list("0123456789")
chars_special = list("!@#$%^&=;:")
colorama.init(autoreset=True)

pass_lenght = 40
try:
    pass_input = sys.argv[1]
    pass_lenght = int(pass_input)
except IndexError:
    print(
        f"{Fore.BLUE}No args — generating {pass_lenght} char long pass{Style.RESET_ALL}"
    )
except ValueError:
    if sys.argv[1] == "--fuck":
        print(f"{Back.RED}{Fore.YELLOW} PROFANE MODE ON ")
        dict_name = "bad-words.txt"
    else:
        print(
            f"[{Fore.RED}{pass_input}{Style.RESET_ALL}] is not a natural number. Using default settings"
        )
except Exception as e:
    print(f"Error: ", e)

words_list = load_dict(dict_name)

password = pick_pass(words_list, pass_lenght - 2)
password.append(choice(chars_numbers) + choice(chars_special))
final_pass = [word.strip("\n") for word in password]
pyperclip.copy("".join(final_pass))
print(f"Pass of {len(pyperclip.paste())} chars copied in the clipboard")

colors = [
    "\x1b[36m",
    "\x1b[32m",
    "\x1b[90m",
    "\x1b[94m",
    "\x1b[96m",
    "\x1b[92m",
    "\x1b[95m",
    "\x1b[91m",
    "\x1b[97m",
    "\x1b[93m",
    "\x1b[35m",
    "\x1b[31m",
    "\x1b[39m",
    "\x1b[37m",
    "\x1b[33m",
]
colored_pass = "".join([choice(colors) + word.strip("\n") for word in password])

print(f"{Back.BLACK}{colored_pass}")
