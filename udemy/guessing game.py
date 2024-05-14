from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, answer, turns):
    ''' checks answer against guess. returns the number of turns remaining'''
    if guess > answer:
        print('too high')
        return turns - 1
    elif guess < answer:
        print('too low')
        return turns - 1
    else:
        print(f'Right! The number is {answer}.')


def set_diff():
    level = input('choose a difficulty. Type "easy" or "hard": ')
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print('number between 1 or 100')
    answer = randint(1, 100)
    # print(f'the right answer is {answer}')

    turns = set_diff()

    guess = 0
    while guess != answer:
        print(f'you have {turns} attempts')
        guess = int(input('Make a guess: '))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('You lose.')
            return
        elif guess != answer:
            print('guess again!')


game()
