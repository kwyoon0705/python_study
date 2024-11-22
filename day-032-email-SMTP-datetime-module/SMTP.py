import smtplib

my_email = ""
my_password = ""
my_msg = "Subject:Hello\n\nHello This is Sending Email using SMTP with Python."

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # email transport layer security
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="", msg=my_msg)
