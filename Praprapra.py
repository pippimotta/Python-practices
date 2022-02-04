print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name_com = name1.lower() + name2.lower()
t = name_com.count('t')
r = name_com.count('r')
u = name_com.count('u')
e = name_com.count('e')
l = name_com.count('l')
o = name_com.count('o')
v = name_com.count('v')

true1 = t + r + u + e
love1 = l + o + v + e

score = true1 * 10 + love1
if score < 10 or score >= 90:
    print(f'Your score is {score}.you go together like coke and mentos.')
elif score <= 50 and score >= 40:
    print(f'Your score is {score}.  you are alright together.')
else:
    print(f'Your score is {score}.')




