from logical_functions import *
from nltk.corpus import words
import sys,re

all_words_list = list(map(lambda word: word.lower(), words.words())) #create list from all english words in lower case

message = input(f"Enter the message to decrypt\n>")
words_in_mess = message.split()

j = 0
decrypt_result = [] 
correct_words = 0 
while j <= 25: #loop going throug all alphabeth
    counter = 0
    decrypt_words = []
    for word in words_in_mess: #loop on words in message
        new_word = decrypt(word, j) #decodes a word based on j
        decrypt_words.append(new_word) #add all of this words in a list
        new_word = re.sub(r"[,.!?:;]","",new_word)
        if new_word.lower() in all_words_list: #count how much of decoded words are in english dictionary
            counter += 1
    else:
        if counter > correct_words: #save results if most matchs were founded
            decrypt_result = decrypt_words.copy()
            correct_words = counter
            key = j
    j += 1

decrypt_message = " ".join(decrypt_result)
print("Key {:>2}: {}".format(key,decrypt_message))