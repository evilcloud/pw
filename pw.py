#!/usr/local/bin/python3

import click
import pyperclip
import sys
import string
import colorama
from colorama import Fore, Back, Style
from random import choice

# @click.command()
# @click.option('--username', '-u', is_flag=True, help='Generates username (default up to 10 charachters)')
# @click.option('--fuck', '-f', is_flag=True, help='Profanity mode')

def load_dict(dict_file):
    ''' Loads dictionary by the file name '''
    word_list = list()
    dict_directory = __file__
    dict_full = dict_directory[:-5] + dict_file
    try:
        with open(dict_full) as txt:
            for i in txt:
                word_list.append(txt.readline())
    except FileNotFoundError:
        print(f"{Back.YELLOW}{Fore.RED}load_dict function error: File {dict_file} not found!")
    except Exception as ex:
        print(ex)
        word_list = ['0']
    return word_list


def generate_random_words(words_list, string_lenght):
    ''' Generates a list of random words from given dictionary up to given lenght '''
    words_container = []
    containter_words_lenght = 0
    while containter_words_lenght != string_lenght:
        words_container.append(choice(words_list).strip().strip("\n").capitalize())
        containter_words_lenght = len("".join(words_container))
        if containter_words_lenght > string_lenght:
            words_container = []
    return words_container

def is_profane(arg_list):
    ''' Checks for the keyword [fuck] in the arguments list and returns True if found '''
    profane = False
    for argument in arg_list:
        if 'fuck' in argument:
            profane = True
    return profane

def parse_argv(arg_list):
    ''' checks arguments for a number, [fuck], and [user] and returns tuple (int, bool, bool) '''
    pass_len = 40
    profane = False
    user = False
    for argument in arg_list:
        if argument.isdigit():
            pass_len = int(argument)
        elif "fuck" in argument:
            profane = True
        elif "user" in argument:
            user = True
    return pass_len, profane, user

def pick_dict(profanity):
    ''' Picks one of the two dictionaries and returns a list of words '''
    return 'bad-words.txt' if profanity else '1-1000.txt'

def genenrate_print_username(user, words_list):
    if user:
        username = "".join(generate_random_words(words_list, 10))
        print(f"\nPrososed username: \n{username}")
    return

def print_profanity_warning(profanity):
    ''' Prints profanity warning '''
    if profanity:
        print(f"{Back.RED}{Fore.YELLOW} PROFANITY MODE ON ")
        return

def main(): # username=False, fuck=False
    ''' A simple prog, that generates password on the fly '''
    chars_numbers = list("0123456789")
    chars_special = list("!@#$%^&=;:")
    colorama.init(autoreset=True)


    pass_lenght, profanity, user = parse_argv(sys.argv)
    dict_name = pick_dict(profanity)
    print_profanity_warning(profanity) if profanity else None
    words_list = load_dict(dict_name)
    genenrate_print_username(user, words_list)
    password = generate_random_words(words_list, pass_lenght - 2) #+ choice(chars_numbers) + choice(chars_special)
    password.append(choice(chars_numbers) + choice(chars_special))
    password = [word.strip("\n") for word in password]
    pyperclip.copy("".join(password))
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

if __name__=="__main__":
    main()