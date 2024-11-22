##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""
# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")
birthday_data_dict = birthday_data.to_dict("records")
now = dt.datetime.now()
now_date = now.date()


def check_birthday():
    for data in birthday_data_dict:
        if data["month"] == now_date.month and data["day"] == now_date.day:
            send_email(data)


def send_email(data):
    with open(file=f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        contents = letter_file.read().replace("[NAME]", f"{data["name"]}")
        print(contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=data["email"], msg=f"Subject:HAPPY BIRTHDAY!!\n\n{contents}")
    return


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

check_birthday()
