import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📄'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')


def display_choices(user_choice, comp_choice):
        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[comp_choice]}')

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and comp_choice == SCISSORS) or 
        (user_choice == SCISSORS and comp_choice == PAPER) or 
        (user_choice == PAPER and comp_choice == ROCK)):
        print('You win')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()
        
        comp_choice = random.choice(choices)

        display_choices(user_choice, comp_choice)

        determine_winner(user_choice, comp_choice)


        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()