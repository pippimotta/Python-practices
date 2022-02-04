#f-string一鍵轉換所有數據類型
#score = 100
#height = 1.62
#isWinning = True
#print(f"Your score is {score},Your height is {height},You are winning is {isWinning}")

print('Welcome to the tip calculator.')
a = input('What was the total bill?\n$')
b = input('What percentage tip would you like to give? 10, 12 or 15?\n')
c = input('How many people to split the bill?\n')

total = float(a) + float(a) * int(b) * 0.01
tip = round(total/int(c), 2)

print(f"Each person should pay: ${tip}")
