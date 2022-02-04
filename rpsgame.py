import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

playerhit = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
pool = ['rock', 'paper', 'scissors']
pool_pic = [rock, paper, scissors]
comhit = random.randint(0,2)
print(pool_pic[playerhit])
print('Computer choose:' + pool_pic[comhit])
if pool[playerhit] == pool[comhit]:
    print('It is a draw')
elif pool[playerhit] == 'rock':
    if pool[comhit] == 'paper':
        print('You lose.')
    else:
        print('You win.')
elif pool[playerhit] == 'paper':
    if pool[comhit] == 'scissors':
        print('You lose')
    else:
        print('You win.')
else:
    if pool[comhit] =='rock':
        print('You lose.')
    else:
        print('You win.')









