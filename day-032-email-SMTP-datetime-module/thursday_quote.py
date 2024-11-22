import random
import smtplib
import datetime as dt


MY_EMAIL = ""
MY_PASSWORD = ""
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open(file="quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    msg = f"Subject:Today's Quote \n\n{quote}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="", msg=msg)


