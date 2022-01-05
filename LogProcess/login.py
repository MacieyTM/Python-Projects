import time
import getpass

username = 'maciej'
password = 'grochowski'

username_input = input('Login: ')
password_input = getpass.getpass('Hasło: ')

def logging():
    if username_input == username and password_input == password:
        print('Prawidłowe dane...')
        print('Proszę czekać...')
        time.sleep(5)
        print('Ok... Ładuję...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        print('Zalogowano pomyślnie!')
    elif username_input == username and password_input != password:
        print('Nieprawidłowe hasło!')
    elif username_input != username and password_input == password:
        print('Nieprawidłowy login!')
    else:
        print('Nieprawidłowy login i hasło!')


if __name__ == "__main__":
    logging()