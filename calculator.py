logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(a, b):
    return a+b
def minus(a, b):
    return a-b
def multiply(a, b):
    return a*b
def division(a,b):
    if b == 0:
        return 'devisor can\'t be zero'
    return a / b
operations = {
    '+': add,
    '-': minus,
    '*': multiply,
    '÷': division
}
def calculator():
    print(logo)

    a = float(input("What's the first number?: "))
    for key in operations:
        print(key)

    not_completed = True

    while not_completed is True:
        operation_symbol = input('pick an operation: ')
        b = float(input('What\'s the next number?: '))
        mid_result = operations[operation_symbol](a, b)
        print(f'{a} {operation_symbol} {b} = {mid_result}')
        proceed = input(f"Type 'y' to continue calculating with {mid_result}, or type 'n' to start a new calculation:")

        if proceed == 'y':
            a = mid_result

        else:
            not_completed = False
            calculator()

calculator()




