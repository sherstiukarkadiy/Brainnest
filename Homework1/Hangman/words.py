from pathlib import Path

WORDS_FILE = Path(__file__).parent.joinpath("words.txt")

with open(WORDS_FILE,'r') as f:
    words_list = f.read().lower().splitlines()
    pass


EASY_LEVEL_WORDS = []
MEDIUM_LEVEL_WORDS = []
HARD_LEVEL_WORDS = []

for word in words_list:
    if len(set(word)) <= 5:
        EASY_LEVEL_WORDS.append(word)
    elif 5 <= len(set(word)) <= 8:
        MEDIUM_LEVEL_WORDS.append(word)
    else:
        HARD_LEVEL_WORDS.append(word)

difficulty_dict = {
    "Easy": EASY_LEVEL_WORDS,
    "Medium": MEDIUM_LEVEL_WORDS,
    "Hard": HARD_LEVEL_WORDS
}

print(len(EASY_LEVEL_WORDS),len(MEDIUM_LEVEL_WORDS),len(HARD_LEVEL_WORDS))