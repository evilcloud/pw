#!/usr/local/bin/python3

import pyperclip
import sys
import string
from random import choice

def load_dict(dict_name):
    ''' Loads dictionary by the file name '''
    word_list = list()
    try:
        with open(dict_name) as txt:
            for i in txt:
                word_list.append(txt.readline())
    except Exception as ex:
        print(ex)
        word_list = ['0']
    return word_list


def get_words_with_stringlenght(words_list, string_lenght):
    ''' Generates a list of random words from given dictionary up to given lenght '''
    words_container = []
    containter_words_lenght = 0
    while containter_words_lenght != string_lenght:
        words_container.append(choice(words_list).strip().strip("\n").capitalize())
        containter_words_lenght = len("".join(words_container))
        if containter_words_lenght > string_lenght:
            words_container = []
    return words_container

def get_random_words(words_list: list, words_num: int =1) -> list:
    random_words = []
    for i in range(words_num):
        random_words.append(choice(words_list).capitalize().strip("\n"))
    return random_words

def generate_num_special(num=1, special=1):
    num_special = ""
    for i in range(num):
        num_special += choice(list('0123456789'))
    for i in range(special):
        num_special+= choice(list("!@#$%^&=;:"))
    return "".join(num_special)

def generate_password(pass_lenght=40):
    password = get_words_with_stringlenght(load_dict('1-1000.txt'), pass_lenght - 2)
    password.append(generate_num_special())
    return password

def generate_username():
    username = get_random_words(load_dict('english-adjectives.txt'))
    username.extend(get_random_words(load_dict('english-nouns.txt')))
    return username
    
def main():
    ''' A simple prog, that generates password on the fly '''
    password = generate_password()
    pyperclip.copy("".join(password))
    # print(f"Pass of {len(pyperclip.paste())} chars copied in the clipboard\n")
    print()
    print("".join(generate_username()))
    print()
    print("".join(password))


if __name__=="__main__":
    main()