##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import smtplib
import datetime as dt
import pandas

my_email = 'lingyizh84@gmail.com'
password = 'muszha__615'

today = dt.datetime.now()

today_tuple = (today.month, today.day)  # 兩個比較記得用tuple！
df = pandas.read_csv('birthdays.csv')
birthdays_dict = {(df_row["month"], df_row["day"]): df_row for (index, df_row) in df.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person['name']

    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as f:
        letter = f.read()
        new_letter = letter.replace('[NAME]', name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person['email'],
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )

# if today.month in list(df.month) and today.day in list(df.day):
#     chosen_1 = df[df.month == today.month]
#     chosen = chosen_1[chosen_1.day == today.day]
#     print(chosen)
#     chosen_dict = {row.name: row.email for (index, row) in chosen.iterrows()}
#     birthday_names = list(chosen_dict.keys())
#
#     for name in birthday_names:
#         chosen_template = random.randint(1, 3)
#         with open(f'letter_templates/letter_{chosen_template}.txt') as f:
#             letter = f.read()
#             new_letter = letter.replace('[NAME]', name)
#             chosen_address = chosen_dict[name]
#         with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs=chosen_address,
#                 msg=f"Subject:Happy Birthday!\n\n{new_letter}"
#             )
