alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

not_end = True

def encrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encypt_word = ''
    for i in range(0, len(text)):
        letter = text[i]
        if text[i] in alphabet:
            new_position = alphabet.index(letter) + shift
            if new_position > 25:
                new_position = new_position % 26
            new_letter = alphabet[new_position]
            encypt_word += new_letter
        else:
            encypt_word += letter
    print('The encode text is ' + encypt_word)

def decrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt_word = ''
    for i in range(0, len(text)):
        letter = text[i]
        if text[i] in alphabet:
            old_position = alphabet.index(letter) - shift
            if old_position < -25:
                old_position = old_position * (-1) % 26
            old_letter = alphabet[old_position]
            decrypt_word += old_letter
        else:
            decrypt_word += letter
    print('The decoded text is ' + decrypt_word)

while not_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode':
        encrypt()
        proceed = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n")
        if proceed == 'No':
            not_end = False
            print('Goodbye')

    elif direction == 'decode':
        decrypt()
        proceed = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n")
    else:
        not_end = False
        exit()
