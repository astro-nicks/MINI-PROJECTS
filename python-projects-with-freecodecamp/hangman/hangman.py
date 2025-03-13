import random
from word import words 

def get_valid_word(words):
    word = random.choice(words)  #randomly chooses something from the list
    while '-' in word '' in word:
        word = random.choice(words)

    return word.upper()