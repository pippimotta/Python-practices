import random
import smtplib
import datetime as dt

my_email = 'lingyizh84@gmail.com'
password = 'muszha__615'

now = dt.datetime.now()
# year = now.year
# date_of_birth = dt.datetime(year=1997, month=6, day=15)
# print(date_of_birth)
if now.weekday() == 2:
    with open('quotes.txt') as quotes_file:
        quotes = quotes_file.readlines()
        quotes_msg = [quote.strip() for quote in quotes]
        chosen_quote = random.choice(quotes_msg)


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='adeleid6@yahoo.com',
            msg=f"Subject:Today's quote\n\n{chosen_quote}"
        )