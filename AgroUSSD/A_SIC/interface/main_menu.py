import json
from pathlib import Path


def display():
    print("\nWelcome to AgroLife!\nWe connect farmers and buyers directly, skip middlemen, and get fair price for all.\n\n1. Register\n2. Login\n3. Exit")

def handle_input(choice):
    if choice == 1:
        user_registration = int(input("\nWelcome!\nWho are you?\n1. Farmer\n2. Buyer\n0. Back to main menu\nChoice: "))
        if user_registration == 1:
            return farmer_registration()
            
        elif user_registration == 2:
            return buyer_registration()
            
        elif user_registration == 0:
            return reset_to_main()


def reset_to_main():
    return display()


def farmer_registration():
    farmer_details_dict = {}
    try:
        print("\n\tYou are about to register as a Farmer.")
        farmer_name = input("Enter your name: ").title()
        farmer_details_dict['Name'] = farmer_name

        farmer_phone_no = input("Enter phone number: ")
        if len(farmer_phone_no) != 11:
            print("Phone number must be 11 digits!")
        else:
            farmer_details_dict['Phone number'] = farmer_phone_no

        farmer_loaction = input("Enter your location: ").title()
        farmer_details_dict['Location'] = farmer_loaction

        farmer_pin = input("Create a 4 digit pin: ")
        if len(farmer_pin) != 4:
            print("Pin must be 4 digits!")
        else:
            farmer_details_dict['Pin'] = farmer_pin

        save_farmer_registration(path, farmer_details_dict)
    except Exception as e:
        print("Error as", e)
    

def buyer_registration():
    buyer_details_dict = {}
    try:
        print("\n\tYou are about to register as a Buyer.")
        buyer_name = input("Enter your name: ").title()
        buyer_details_dict['Name'] = buyer_name

        buyer_phone_no = int(input("Enter phone number: "))
        if len(buyer_phone_no) != 11:
            print("Phone number must be 11 digits!")
        else:
            buyer_details_dict['Phone number'] = buyer_phone_no

        buyer_loaction = input("Enter your location: ").title()
        buyer_details_dict['Location'] = buyer_loaction

        buyer_pin = int(input("Create a 4 digit pin: "))
        if len(buyer_pin) != 4:
            print("Pin must be 4 digits!")
        else:
            buyer_details_dict['Pin'] = buyer_pin

        return "Account successfully created!"
    except Exception as e:
        print("Error as", e)


workspace = Path("Farmer_Details")
workspace.mkdir(exist_ok=True)
path = workspace / "Farmer.json"

def save_farmer_registration(path, farmer_details_dict):
    farmer_details_dict ={}
    with open(path, "w", newline="", encoding="utf-8") as f:
        json.dump(farmer_details_dict, f, indent=2)
    print("Information saved to data base.")

def load_farmer_registration(path):
    with open(path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        print(loaded_data)