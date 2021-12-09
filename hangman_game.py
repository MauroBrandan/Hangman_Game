import random
from os import system

def game(word):
    word_game = word
    correct_words = ['_' for letter in word_game]
    user_word = ''
    
    while ''.join(correct_words) != word_game:
        try:
            print('Adivina la palabra')
            print(' '.join(correct_words))
            user_word = input('Ingresa una letra: ').upper()
        
            if len(user_word) > 1 or user_word.isdigit():
                raise ValueError

            for i, letra in enumerate(word_game):
                if word_game[i] == user_word:
                    correct_words[i] = user_word
            
            system("cls")
        
        except ValueError:
            system("cls")
            print('ERROR: Ingresa solo una letra')

    print(f'Ganaste!! La palabra era {word_game}')


def normalize(word):
    table = word.maketrans('áéíóú', 'aeiou')
    word_game = word.translate(table).upper()
    return word_game


def selectWord(words):
    number_random = random.randint(1, len(words))
    word = words[number_random]
    word = normalize(word)
    return word
    

def getData():
    words = []
    with open('data.txt', 'r', encoding='utf-8') as f:
        words = [word.replace('\n', '') for word in f]
    return words


def run():
    words = getData()
    word = selectWord(words)
    game(word)


if __name__ == '__main__':
    run()
