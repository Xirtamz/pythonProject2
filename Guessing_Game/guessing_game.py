from art import logo, vs
from guess_data import data
import random
from replit import clear

# format the account data into printable format.
def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_descr}, from {account_country}'


def check_answer(guess, a_followers, b_followers): # take the user guess and follower counts, return if right
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# make the game repeatable.

while game_should_continue:
    # generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)}')
    print(vs)
    print(f'Against B: {format_data(account_b)}')

    # Ask user for a guest
    guess = input('Who has more followers? Type "A" or "B": ').lower()

    # check if user is correct.
    ## get follower count of each account.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    ## use if statement to check if user is correct.
    # Score keeping.
    # give usr feedback on their guess.
    if is_correct:
        score += 1
        print('You are right')
    else:
        game_should_continue = False
        print(f'thats wrong. Final score {score}')




# making account at position B become the next account at position A

# clear the screen between rounds