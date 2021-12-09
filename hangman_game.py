import random
from os import system

# Documentacion:
# How to Check if an item exists in list: https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
# La función enumerate(): https://micro.recursospython.com/recursos/la-funcion-enumerate.html
# Metodo Get de diccionarios: https://uniwebsidad.com/libros/python/capitulo-8/metodos-de-retorno
# Listas en Python: https://devcode.la/tutoriales/listas-python/

# def prueba():
#     letras = ['P', 'A', 'L', 'T', 'A']
#     print(letras)
#     if 'M' in letras:
#         print('Yessss')
#     else:
#         print('Nouuu')


def game(word):
    word_game = word
    correct_words = ['_' for letter in word_game]
    user_word = ''

    #Tengo que ver como hago para comparar las dos listas, la de las letras correctas y la de las letras de la palabra
    #Buscar alguna funcion de listas en la que se peuda verificar si contine determinado elemento
    
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
    # print(words)
    return words


def run():
    # print(menu)
    words = getData()
    word = selectWord(words)
    game(word)


if __name__ == '__main__':
    run()
    #prueba()