# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt') as name_file:
    name_list = name_file.readlines()
    name_list = [name.strip() for name in name_list]

with open('Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

for name in name_list:
    with open(f'Output/ReadyToSend/Letter to {name}.txt', 'w') as new_file:
        new_letter = letter.replace('[name]', name)
        new_file.write(new_letter)

