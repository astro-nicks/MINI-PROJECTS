import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y': 
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice =='n':
        print('Thanks for playing!')
        
    else: 
        print('Invalid choice')
        return

# Ask: roll the dice
# If user generates y
#  Generate two random numbers
#   Print them
# If user enters n 
#   Print thank you message
#   Terminate
# Else 
#   Print invalid choice