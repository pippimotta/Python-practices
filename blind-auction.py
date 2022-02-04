logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

print('Welcome to the secret auction program.')
auction_pool = {}
not_finished = True
max = 0
def bid_process():
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    auction_pool[name] = bid
while not_finished is True:
    bid_process()
    proceed = input("Are there any other bidders? Type 'Yes' or'No'.")

    if proceed == 'No':
        not_finished = False


for name in auction_pool:
    if auction_pool[name] > max:
        max = auction_pool[name]
        big_bidder = name
print(f'The winner is {name} with a bid of ${max}.')