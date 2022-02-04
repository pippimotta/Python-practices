import pandas
nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

# 生成dictionary
# letter_list = [row.letter for (index, row) in nato_df.iterrows()]
# code_list = [row.code for (index, row) in nato_df.iterrows()]
# nato_dic = dict(zip(letter_list, code_list))
nato_dic = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dic)
# interface
not_input = True
while not_input:
    user_name = input('What is your name?\n').upper()
    try:
        transferred = [nato_dic[letter] for letter in user_name]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        not_input = False
        print(transferred)



