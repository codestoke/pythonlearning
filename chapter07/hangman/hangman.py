import random  # this is useful for selecting a word from a list

used_letters = ""
the_word = ""


def get_secret_word():
    return "secret word"


def print_used_chars():
    print(used_letters)


def print_secret_word():
    print(the_word)


def print_hangman():
    hangman = '''
    /-----\\
    |     |
    |     0
    |    \\/
    |     |
    |    /\\
    |
    |
    ==========
    '''
    print(hangman)
    print_secret_word()
    print_used_chars()


def ask_for_next_letter():
    return 0
