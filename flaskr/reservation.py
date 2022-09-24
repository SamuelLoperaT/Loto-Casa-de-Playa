import pandas as pd
import os
from os.path import exists
import datetime

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

if exists(f'{__location__}/reservations.csv'):
    reservations = pd.read_csv(f'{__location__}/reservations.csv')
else:
    dir_list = os.listdir(__location__)
    print(dir_list)
    reservations = {
        "NAME": [],
        "CITY": [],
        "CONTACT_NUMBER": [],
        "E-MAIL": [],
        "PAY_CONFIRMATION": [],
        "PAY_DATE": [],
        "RESERVATION_START": [],
        "RESERVATION_END": [],
        "NUMBER_OF_PEOPLE": []
    }
    with open(f'{__location__}/reservations.csv', "w") as fp:
        pass
    dir_list = os.listdir(__location__)
    print(dir_list)
    resv = pd.DataFrame(reservations)
    resv.to_csv(f'{__location__}/reservations.csv')
    print("Successful csv Creation")


def add_reservation(name, city, contact_number, e_mail, confirmation, paydate, reservation_start, reservation_end,
                   number_of_people):
    reservation_data = {
        "NAME": [name],
        "CITY": [city],
        "CONTACT_NUMBER": [contact_number],
        "E-MAIL": [e_mail],
        "PAY_CONFIRMATION": [confirmation],
        "PAY_DATE": [paydate],
        "RESERVATION_START": [reservation_start],
        "RESERVATION_END": [reservation_end],
        "NUMBER_OF_PEOPLE": [number_of_people]
    }
    reservation = pd.DataFrame(reservation_data)
    pd.concat([reservations, reservation])
    reservation.to_csv(f'{__location__}/reservations.csv')

