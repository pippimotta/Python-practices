def check_prime_number():
    number = int(input('Please enter a number\n'))
    k = 0
    if number == 1 or number == 2:
        print('It\'s a prime number.')
    else:
        for i in range(2, number):
            test = number % i
            if test == 0:
                k += 1

        if k != 0:
            print('It\'s not a prime number.')
        else:
            print('It\'s a prime number.')
check_prime_number()

#better choice
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")