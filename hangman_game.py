import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letters_picked = ''
numbers_picked = ''
symbols_picked = ''
for letter in range(0, nr_letters+1):
    m = random.randint(0, len(letters)-1)#letters_picked =+ random.choice(letters)
    letters_picked = letters_picked + letters[m]

for number in range(0, nr_numbers+1):
    n = random.randint(0, len(numbers)-1)
    numbers_picked = numbers_picked + numbers[n]

for symbol in range(0, nr_symbols+1):
    k = random.randint(0, len(symbols)-1)
    symbols_picked = symbols_picked + symbols[k]

pri_password = letters_picked + symbols_picked + numbers_picked
fin_password = ''.join(random.sample(pri_password, len(pri_password)))#打亂字串順序
print(f'Your password is' + fin_password)

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")


————————————————————————
import random
word_list = ['kangaroo', 'baboon', 'capybara', 'panda', 'butterfly', 'cicada', 'sudachi', 'zombie']
chosen_word = random.choice(word_list)
fluency = len(chosen_word)
generator = []
for i in range(0, fluency):
    generator.append('_')
print(generator)
game_is_finished = False
lives = fluency


while not game_is_finished:
    input_letter = input('guess a letter:\n')
    if input_letter in generator:
        print('you have already guessed   ' + input_letter)
    for position in range(fluency):
        test = chosen_word[position]
        if input_letter == test:
            generator[position] = input_letter
    print(generator)

    if input_letter not in chosen_word:
            print('one step closer to death')
            lives = lives - 1
            if lives == 0:
                game_is_finished  = True
                print(chosen_word + 'you lose hahaha')

    if not '_' in generator:
        game_is_finished = True
        print("You win.")
