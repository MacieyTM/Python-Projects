import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    return word.upper()

print('')
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        if lives == 7:
            print('Pozostało', lives, 'prób.')
        else:
            print('Pozostało', lives, 'prób. Użyte litery:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Obecne słowo:', ' '.join(word_list))

        user_letter = input('Zgadnij literę: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\nTwoja litera', user_letter, 'nie znajduje się w słowie.')

        elif user_letter in used_letters:
            print('\nJuż użyłeś tej litery. Spróbuj użyć innej.')

        else:
            print('\nTo nie jest dozwolona litera.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('Przegrałeś! Odpowiedź:', word)
    else:
        print('Gratulacje! Zgadłeś słowo:', word, '!!')


if __name__ == '__main__':
    hangman()