from functions import *

while True:
    game_play = bool(input("To start press any key + Enter: "))
    if not game_play:
        break
    print(game(random_word(difficulty_level_choose())))
