import random
print('Welcome to hangman game.')
pool = ['baboon', 'sudachi', 'zombie','capybara','butterfly','cicada','gorilla', 'spider']
chosen_word = random.choice(pool)
game_not_over = True
lives = len(chosen_word)
interface = []
for i in range (0, len(chosen_word)):
    interface.append('_')
print(interface)


while game_not_over is True:
    input_letter = input('Please enter a letter:\n')

    if input_letter in interface:
        print('You have already tried this letter')
    for position in range(0, len(chosen_word)):
        test = chosen_word[position]
        if test == input_letter:
            interface[position] = input_letter
    print(interface)
    if not '_' in interface:
        game_not_over = False
        print('You win.')


    if input_letter not in chosen_word:
        lives -= 1
        print('one step closer to death')
        if lives == 0:
            game_not_over = False
            print('You lose.')



