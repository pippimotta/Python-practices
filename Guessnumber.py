import random
answer = random.randint(1, 100)
def guess_number(guess, answer):
    if guess != answer:
        if guess > answer:
            print('Too high.')
        else:
            print('Too low')
    else:
        print('Bingo!')
not_completed = True
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    lives = 10
if level == 'hard':
    lives = 5

while not_completed:
    print(f'You have {lives} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    lives -= 1
    guess_number(guess, answer)
    if lives == 0:
        not_completed = False
        print('You got run out of your lives. You lose. ')

    if guess == answer:
        not_completed = False
        print(f'You win! The answer is {answer}')



