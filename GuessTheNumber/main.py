import random
import time

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Zgadnij liczbę z zakresu (1-{x}): '))
        if guess < random_number:
            print('\nZa mała.')
        elif guess > random_number:
            print('\nZa duża.')

    print(f'\nGratulacje, zgadłeś liczbę {random_number}, którą wymyśliłem!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'p':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Czy {guess} za duża (d), za mała (m), czy poprawna (p)? ')
        if feedback == 'd':
            high = guess - 1
        elif feedback == 'm':
            low = guess + 1

    print(f'\nJa (komputer) zgadłem twoją liczbę {guess}, którą wymyśliłeś!')


if __name__ == "__main__":
    y=int(input('\nPrzykładowe zakresy:\n10 to zakres (1-10)\n100 to zakres (1-100)\n\nPodaj zakres w jakim chcesz grac: '))
    print(f'\nSpróbuj zgadnąć liczbę z zakresu (1-{y}), którą ja (komputer) wymyśliłem z tego zakresu.')
    guess(y)
    print(f'\nTeraz ty wymyśl liczbę z tego samego zakresu (1-{y}). Za 10 sekund ja (komputer) spróbuję ją zgadnąć.')
    time.sleep(10)
    computer_guess(y)