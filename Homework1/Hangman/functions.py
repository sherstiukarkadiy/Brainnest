from words import difficulty_dict
import random
import re


def create_menu(dict: dict) -> str:
    """Create menu with difficulty levels

    Args:
        dict (dict): Variations dictionary

    Returns:
        str: menu
    """
    header = "|{:^14}|".format("Menu")
    spliter = "-"*16
    board = ""
    num = 1
    for level in dict:
        board += "|{:^3}|{:^10}|\n".format(num, level)
        num += 1
    menu = f"{spliter}\n{header}\n{spliter}\n{board}{spliter}"
    return menu


def difficulty_level_choose(dict: dict) -> str:
    """Allows the user to choose difficlty level
    
    Args:
        dict (dict): Variations dictionary

    Returns:
        str: difficlty level
    """
    print(create_menu())
    while True:
        try:
            level_choose = int(input("Choose difficulty level from 1 to 3: "))
        except:
            print("Not correct value")
            continue

        if level_choose < 1 or level_choose > 3:
            print("Not in diapasone")
            continue
        break
    level_choose = list(difficulty_dict.keys())[level_choose-1]
    return level_choose


def random_word(difficulty_level: str) -> str:
    """Choose random word from choosed dificulty level

    Args:
        difficulty_level (str): difficlty level

    Returns:
        str: word
    """
    words_list = difficulty_dict[difficulty_level]
    word = random.choice(words_list)
    return word


def substitute_word(word: str, letter_set: set) -> str:
    """Substitute not guessed letters from word by "_" for game function

    Args:
        word (str): game word
        letter_set (set): set of not guessed letters from game word

    Returns:
        str: word without unguessed letters
    """

    for letter in letter_set:
        word = re.sub(letter, "_", word)
    return word


def game(word: str) -> str:
    """Hangmang game

    Args:
        word (str): game word

    Returns:
        str: game result table
    """
    mistakes_left = 6
    used_letters = []
    spaced_word = word
    letter_set = set(word)

    for letter in letter_set:
        spaced_word = re.sub(letter, f"{letter} ", spaced_word)

    game_line = substitute_word(spaced_word, letter_set)

    while mistakes_left > 0:
        print(
            f"\nYou have {mistakes_left} tries left.\nUsed letters: {' '.join(used_letters)}\nWord: {game_line}")
        while True:
            user_letter = input("Guess a letter: ")
            if (not user_letter.isalpha()) or (len(user_letter) != 1) or (user_letter in used_letters):
                print("Not correct input, one more time")
                continue
            break
        try:
            letter_set.remove(user_letter.lower())
        except:
            mistakes_left -= 1
        else:
            if len(letter_set) == 0:
                return "\n{:-^16}\n{:'^16}\n{:^16}\n{:-^16}".format("", word, "YOU WON", "")
            game_line = substitute_word(spaced_word, letter_set)
            pass
        used_letters.insert(0, user_letter)
    else:
        return "\n{:-^16}\n{:'^16}\n{:^16}\n{:-^16}".format("", word, "YOU LOOSE", "")
