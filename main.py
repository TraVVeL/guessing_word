import json
import random

with open('russian_nouns_with_definition.json', encoding='utf-8') as f:
    jsondict = json.load(f)


def restart():

    def get_word():
        dict_length = len(list(jsondict)) - 1
        ran_digit = random.randint(0, dict_length)

        word_rus = list(jsondict)[ran_digit]
        word_rus = word_rus.upper()

        hint_word = jsondict.get(list(jsondict)[ran_digit]).get("definition")
        return word_rus, hint_word

    def display_hangman(tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            ''',
            # голова, торс, обе руки, одна нога
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            ''',
            # голова, торс, обе руки
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            ''',
            # голова, торс и одна рука
            '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            ''',
            # голова и торс
            '''
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            ''',
            # голова
            '''
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            ''',
            # начальное состояние
            '''
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            '''
        ]
        return stages[tries]

    display_hangman(tries=6)

    def play(word):
        word_completion = '▮' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
        guessed_letters = []  # список уже названных букв
        guessed_words = []  # список уже названных слов
        tries = 6
        print('Let\'s play a game')
        print(display_hangman(tries))
        print(f'Suggested word: {word_completion} have numbers of letters: {len(word)} \n'
              f'and number of attempts is: {tries}')

        while True:
            latter = input('Input your latter: ').upper()

            if not latter.isalpha():
                print('Input a real latter')
                continue

            if latter in [*guessed_letters, *guessed_words]:
                print(f'This latter/word is already in a list try another one')

                continue

            if latter not in guessed_words and len(latter) > 1:
                guessed_words.append(latter)
                tries -= 1

            if latter not in word and len(latter) == 1:
                guessed_letters.append(latter)
                tries -= 1
            elif latter in word:
                guessed_letters.append(latter)

            if latter in word:
                for i in range(len(word)):
                    if word[i] == latter:
                        word_completion = word_completion[:i] + latter + word_completion[i + 1:]
            if word == word_completion or word in guessed_words and tries >= 1:
                print(f'Congratulations! \n'
                      f'remaining attempts: {tries}')
                break
            if tries == 1:
                get_hint = input('Wanna get a hint? (да, ye, + yes, y or Enter\\Any key to continue): ')
                if get_hint.lower() in ['yes', '+', 'да', 'ye', 'y', '']:
                    print(get_word()[1])
                    continue

            if tries <= 0:
                print(f'You almost did it! The word was: {word}')
                print(display_hangman(tries=0))
                break
            print(f'your guess: {word_completion} Numbers of attempts: {tries}')
            print(display_hangman(tries))

    play(get_word()[0])
    answer = input('Want to play the game again? (да, ye, + yes, y or Enter\\Any key to end the game): ')
    if answer.lower() in ['yes', '+', 'да', 'ye', 'y', '']:
        return restart()

    else:
        print('See you later!')
        return False


restart()
