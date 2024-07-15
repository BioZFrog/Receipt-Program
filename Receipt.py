from datetime import datetime
now = datetime.now()
import os

print("\nWELCOME TO BURGER RESTAURANT\n")

file_path = 'bill.txt'

if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write('0')

with open(file_path, 'r') as file:
    number = int(file.read())

number += 1

with open(file_path, 'w') as file:
    file.write(str(number))


try:
    Burger = input("How many burgers for today? ")
    Burger_am = int(Burger) * 17.00

    type = input("Chicken or beef? (chicken, beef) ")

    anything = input("Anything Else? (ketchup, fires) ")

    anything_am = input(f"How many {anything}? ")
    anything_am = int(anything_am)  

    pay = input("Great! Now how will you like to pay? (card, cash) ")

    if anything.lower() == "ketchup":
        Total = Burger_am + anything_am * 0.25
    elif anything.lower() == "fries":
        Total = Burger_am + anything_am * 5.00

    card = Total if pay == 'card' else 0.00
    cash = Total if pay == 'cash' else 0.00

    Reciept = f"""
                 BURGER RESTAURANT ONLINE 
                     TEL : 000000000
             

Served by : Admin
{now.day}-{now.month}-{now.year} {now.strftime("%I:%M %p")}
Bill # {number}
-----------------------------------------------------
DESCRIPTION                   QTY            AMOUNT
-----------------------------------------------------
{type.upper()} BURGER                   {Burger}               {Burger_am}
{anything.upper()}                         {anything_am}               {anything_am * (1.00 if anything.lower() == 'ketuchup' else 0.25 if anything.lower() == 'fires' else 5.00)}
-----------------------------------------------------
Total QTY : {int(Burger) + anything_am}

                Bill Amount :               {Total}
                Paid Method (VISA CARD) :   {card}
                Bal. Amt. (USD)   :         {cash}
                
Thank you. Please Visit Again
                          """

    print(Reciept)
except:
    print("\nOrder cancelled")
