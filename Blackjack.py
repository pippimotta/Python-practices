import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

cards_pool = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card_generagtor():
    return random.choice(cards_pool)


def new_card(cards):
    cards.append(card_generagtor())
    return cards


def card_score(cards, total=0):#用sum sum(iterable[, start])
    for card in cards:
        total += card
    return total



def blackjack():
    welcome = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if welcome == 'y':
        not_completed = True
        print(logo)
        user_card1 = card_generagtor()
        user_card2 = card_generagtor()
        user_cards = [user_card1, user_card2]
        user_score = card_score(user_cards)
        com_card1 = card_generagtor()
        com_card2 = card_generagtor()
        com_cards = [com_card1, com_card2]
        com_score = card_score(com_cards)
        if user_score == 21:
            not_completed = False
            print("Wow! You got blackjack. You win")
        if com_score == 21:
            not_completed = False
            print('opponent has Blackjack,You lose. ')
        while not_completed:
            if 11 in user_cards:
                if user_score > 21:
                    user_score -= 10
                    user_cards.remove(11)
                    user_cards.append(1)
            print(f'Your cards: {user_cards}, current score: {user_score}')
            print(f"Computer's first card: {com_card1}")
            proceed = input("Type 'y' to get another card, type 'n' to pass: ")

            if proceed == 'n':
                not_completed = False
                while com_score < 17:
                    com_cards = new_card(com_cards)
                    com_score = card_score(com_cards)
                if com_score > 21:
                    print('computer got bust. You win.')
                    print(f"Computer's final hand: {com_cards}, final score:{com_score}")
                if user_score == 21:
                    if com_score != 21:
                        print(f"Computer's final hand: {com_cards}, final score:{com_score}")
                        print('You got 21, you win, congratulations!')
                    else:
                        print('You got 21, you win, congratulations!')
                        print("Computer also got 21. It's a draw.")

                if user_score < 21 and com_score < 21:
                    print(f"Your final hand: {user_score},final score: {user_score}")
                    print(f"Computer's final hand: {com_cards}, final score:{com_score}")
                    if user_score > com_score:
                        print("You win. Congratulations.")
                    elif user_score < com_score:
                        print('You lose.')
                    else:
                        print("It is a draw.")


            else:
                user_cards = new_card(user_cards)
                user_score = card_score(user_cards)

                if user_score > 21:
                    not_completed = False
                    print(f"Computer's final hand: {com_cards}, final score:{com_score}")
                    print(f"Your final hand: {user_cards}, final score:{user_score}")
                    print('You bust and you lose.')
                elif user_score == 21:
                    not_completed = False
                    print('You got 21, you win, congratulations!')
        blackjack()
    else:
        print('Goodbye!')


blackjack()
