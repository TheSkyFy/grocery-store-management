import re
from datetime import *


items = [{"id": 101, "Name":"Amul Milk (500ml)", "Price":"50"},
       {"id":102, "Name":"Brown Bread", "Price":"40"},
       {"id":103, "Name":"Eggs Tray (12pc)", "Price":"70"},
       {"id":104, "Name":"Nestle Yogurt (300gm)", "Price":"100"},
       {"id":105, "Name":"MD fresh paneer", "Price":"80"},
       {"id":106, "Name":"Amul butter", "Price":"30"},
       {"id":107, "Name":"Onion (1kg)", "Price":"20"},
       {"id":108, "Name":"Potato (1kg) ", "Price":"30"},
       {"id":109, "Name":"Carrot (500gm)", "Price":"60"},
       {"id":110, "Name":"Apple (200gm)", "Price":"40"},
       {"id":111, "Name":"Mango (200gm)", "Price":"90"},
       {"id":112, "Name":"Banana (250gm)", "Price":"100"},
       {"id":113, "Name":"Atta (10kg)", "Price":"400"},
       {"id":114, "Name":"Basmati Rice (5kg)", "Price":"300"},
       {"id":115, "Name":"Mustard Oil (1L)", "Price":"150"},
       {"id":116, "Name":"Toor Dal (500g)", "Price":"100"},
       {"id":117, "Name":"Olive oil (1L)", "Price":"200"}]              

shopping = items

cart = []
order = ""

def get_phone():
    print("-------------------WELCOME TO FERGO STORE--------------------\n")
    number = int(input('Please type in your phone number.\n>'))
    print()
    mod_val = number % 1000000000 
    
    if not(mod_val < 1000000000 and mod_val != number):
        print('Phone number is invalid.\n')
        number = get_phone()
    
    return number

def get_email():
    email = input('Please type in your email.\n>')
    print()
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not(re.fullmatch(email_regex, email)):
        print('Email is invalid.\n')
        email = get_email()

def get_pin_code():
    pin_code_regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
    pin_code = input('Please type your pincode.\n>')
    print()
    
    if not(re.fullmatch(pin_code_regex, pin_code)):
        print('Invalid pincode.\n')
        pin_code = get_pin_code()

    return pin_code

def get_address():
    addinput = input("Please enter your address.\n>")
    print()

def LoginWindow():
    print("\n=====================\n")
    print("1.Display Menu")
    print("2.Cart")
    print("3.Remove item")
    print("4.Place order")
    print("5.Exit")
    print("\n======================\n")

def DisplayMenuWindow():
  
    print("Id\tName\tQuantity\tPrice")
    print("====================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Price"]}')

    p_id = int(input("\nEnter the id\n>"))
    
    for d in shopping:
        if d["id"] == p_id:
            print("\n\nId\tName\tQuantity\tPrice(in ₹)")
            print("=============================================================")
            print(f'{d["id"]}\t{d["Name"]}\tQuantity\t\t{d["Price"]}')
            order = (f'{d["id"]}\t{d["Name"]}\t\t{d["Price"]}')
            order2 = (f'{d["Name"]}')
            confirm = input("\nDo you want to add item to cart, Y/N\n> ")
            if confirm == 'Y' or confirm == 'y':
                cart.append(order2)
                print("Your item has been added to cart")


def shop_cart():
    print(cart)
    

def deli_date():
    today = date.today()
    Begindate = today
    Enddate1 = Begindate + timedelta(days=3)
    Enddate2 = Begindate + timedelta(days=2)
    Enddate3 = Begindate + timedelta(days=1)
    print("Ending date")
    print(f'1. {Enddate1}\n2. {Enddate2}\n3. {Enddate3}\n')
    abcd = input("Choose delivery date from above\n>")
    if abcd =='1':
        print(f'Thank you, your order will be deliver by {Enddate1}') 
    elif abcd =='2':
        print(f'Thank you, your order will be deliver by {Enddate2}')
    elif abcd =='3':
        print(f'Thank you, your order will be deliver by {Enddate3}')


def remove_items():
    shop_cart()
    rev =input("Enter the name need to be deleted\n>")
    if rev in cart:
        conf = input(f'\nAre you sure to remove {rev} from cart, Y/N\n>')
        if conf == 'Y' or conf == 'y': 
            cart.remove(rev)
            print(cart)
            LoginWindow()
            ChoiceOptions()
        else:
            LoginWindow()
            ChoiceOptions()
    else:
        print('Invalid name. Item not present in cart')
        remove_items()
        



def place_order():
    opt = input("Do you want to place order, Y/N\n>")
    if opt == 'Y' or opt == 'y':
        shop_cart()
        deli_date()
    
    else:
        LoginWindow()
        ChoiceOptions()

def ChoiceOptions():
    choice = int(input("Please enter choice\n>"))
    print
    if choice == 1:
        DisplayMenuWindow()
        LoginWindow()
        ChoiceOptions()
    elif choice == 2:
        shop_cart()
        LoginWindow()
        ChoiceOptions()
    elif choice == 3:
        remove_items()
    elif choice == 4:
        place_order()
    else:
        print("Invalid Choice. Please enter valid choice")

def run():
    get_phone()
    get_email()
    get_pin_code()
    get_address()
    LoginWindow()
    ChoiceOptions()

run()