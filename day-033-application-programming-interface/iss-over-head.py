import requests
import smtplib
import time
import datetime as dt

ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
MY_LAT = 39.036536260737826
MY_LNG = 125.73107691828159

MY_EMAIL = ""
MY_PWD = ""


def estimate_position():
    res_iss_location = requests.get(url=ISS_API_ENDPOINT)
    res_iss_location.raise_for_status()
    res_iss_location.json()

    iss_latitude = float(res_iss_location.json()["iss_position"]["latitude"])
    iss_longitude = float(res_iss_location.json()["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        send_email()
    else:
        print(f"Not yet.. Now time is {dt.datetime.now()}")
        print(f"Your position is {MY_LAT}, {MY_LNG}")
        print(f"The ISS's position is {iss_latitude}, {iss_longitude}")
        return


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PWD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="Subject:Look Up!!!\n\nThe ISS is above you in the sky!!!")
    return


while True:
    time.sleep(10)
    estimate_position()
