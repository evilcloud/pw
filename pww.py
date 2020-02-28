#!/usr/local/bin/python3

import os

# import pyperclip
import string
from random import choice, randint

import consts


def app_dir() -> str:
    """Returns the full path of the current app
    
    Returns:
        str -- [full absolute path]
    """
    directory, _ = os.path.split(os.path.abspath(__file__))
    return directory


def validate_dir(directory: str):
    """Checks for the existence of a directory, and if negative, creates it
    
    Arguments:
        directory {str} -- [directory name]
    """
    full_dir = os.path.join(app_dir(), directory)
    if not full_dir:
        os.mkdir(full_dir)
    return


def is_file(file_name: str, directory: str = "") -> bool:
    """Checks if file exists (directory optional)
    
    Arguments:
        file_name {str} -- [name of the file to check]
    
    Keyword Arguments:
        directory {str} -- [optional directory] (default: {""})
    
    Returns:
        bool -- [boolean return]
    """
    if os.path.isfile(os.path.join(app_dir(), directory, file_name)):
        return True
    else:
        return False


def strip_words(word_list: list) -> list:
    """Returns same list, with each item stripped of spaces, nextlines and tabs
    
    Arguments:
        word_list {list} -- [list to be cleaned]
    
    Returns:
        list -- [clean list]
    """
    return [word.strip().strip("\n").strip("\t") for word in word_list]


def capitalize_list(word_list: list) -> list:
    """Returns the list with each word capitalized
    
    Arguments:
        word_list {list} -- [list to be capitalized]
    
    Returns:
        list -- [list with capitalized items]
    """
    return list(map(lambda word: word.capitalize(), word_list))


def get_wordlist(dict_name: str) -> list:
    """Loads all words from a provided dictionary and returns them in a list
    
    Arguments:
        dict_name {str} -- [dictionary file name]
    
    Raises:
        SystemExit: [No dictionary found -- abort program]
    
    Returns:
        list -- [each word as an entry in a flat dictionary]
    """
    dictionaries_dir = consts.DICT_DIR
    words_list = []
    if not is_file(dict_name, dictionaries_dir):
        print(f"Dictionary {dict_name} is not found in directory {dictionaries_dir}")
        raise SystemExit
    try:
        with open(os.path.join(dictionaries_dir, dict_name), "r") as dic:
            words_list = dic.readlines()
    except Exception as ex:
        print(f"Error accessing")
        print(ex)
    return strip_words(words_list)


def random_words_number(word_list: list, number: int) -> list:
    """Returns a list of randomly generated words from given word list. Number is also given
    
    Arguments:
        word_list {list} -- [word list subject to choice]
        number {int} -- [number of words randomly picked from the word list]
    
    Returns:
        list -- [list of randomly picked words from the word list]
    """
    words = []
    for i in range(number):
        words.append(choice(word_list))
    return words


def random_words_lenght(
    word_list: list, lenght: int = consts.PASS_DEFAULT_WORD_LENGTH
) -> list:
    """Returns a list of randomly picked words from the word list of predetermined total lenght 
    
    Arguments:
        word_list {list} -- [word list]
    
    Keyword Arguments:
        lenght {int} -- [total lenght of all elements in the list] (default: {consts.PASS_DEFAULT_WORD_LENGTH})
    
    Returns:
        list -- [list of randomly picked words]
    """
    words = []
    words_lenght = 0
    while words_lenght != lenght:
        words.append(choice(word_list))
        words_lenght = len("".join(words))
        if words_lenght > lenght:
            pop_number = randint(0, len(words) - 1)
            words.pop(pop_number)
    return words


def generate_username() -> list:
    """Returns a list of randomly picked adjective and a noun
    
    Returns:
        list -- [list consisting of an ajdective and a noun]
    """
    adjectives = get_wordlist(consts.DICT_ADJECTIVES)
    nouns = get_wordlist(consts.DICT_NOUNS)
    username = random_words_number(adjectives, 1)
    username.extend(random_words_number(nouns, 1))
    return capitalize_list(username)


def random_num() -> list:
    """Returns a list with a single value of a ranomly picked digit
    
    Returns:
        list -- [random digit]
    """
    return [choice(list("0123456789"))]


def random_special() -> list:
    """Returns a list with a single randomly picked special charachter
    
    Returns:
        list -- [random special char]
    """
    return [choice(list("!@#$%^&*()+=?"))]


def generate_password(
    lenght: int = consts.PASS_DEFAULT_WORD_LENGTH, profane: bool = consts.PASS_PROFANE
) -> list:
    if profane:
        total_wordlist = get_wordlist(consts.DICT_PROFANITIES)
    else:
        total_wordlist = get_wordlist(consts.DICT_ADJECTIVES) + get_wordlist(
            consts.DICT_NOUNS
        )
    return capitalize_list(
        random_words_lenght(total_wordlist)
    )  # + random_num() + random_special


def main():
    # adjectives = get_wordlist(consts.DICT_ADJECTIVES)
    # bad_words = get_wordlist(consts.DICT_PROFANITIES)
    # nouns = get_wordlist(consts.DICT_NOUNS)

    # test_dict = nouns + adjectives
    # num_ran = (capitalize_list(random_words_number(test_dict, 10)))
    # print(num_ran, len(num_ran))
    # len_ran = (capitalize_list(random_words_lenght(test_dict)))
    # print(len_ran, len("".join(len_ran)), "\n", "".join(len_ran))
    print(generate_username())
    print(generate_password())


if __name__ == "__main__":
    main()
