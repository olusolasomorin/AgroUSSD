import json
from pathlib import Path


def display():
    print("\nWelcome to AgroLife!\nA place where farmers and buyers connect directly, skip middlemen, and get fair price for all.\n\n1. Register\n2. Login\n0. Exit")

def handle_input(choice):
    if choice == 1:
        user_registration = int(input("\nWelcome!\nDo you want to register as a farmer or buyer?\n1. Farmer\n2. Buyer\n00. Back to main menu\nChoice: "))
        if user_registration == 1:
            return farmer_registration()
            
        elif user_registration == 2:
            return buyer_registration()
            
        elif user_registration == 00:
            return reset_to_main()
        
    # elif choice == 2:
    #     user_login = int(input("\nWho do you want to login as?\n1. Farmer\n2. Buyer\n00. Back to main menu\nchoice: "))
    #     if user_login == 1:
    #         # return farmer_login()


def reset_to_main():
    return display()


# Saving and loading user details in a jason file
# Create a file if it doesn't exist
workspace = Path("Farmer_Details")
workspace.mkdir(exist_ok=True)
path = workspace / "Farmer.json"

# Save users to file
def save_farmer_registration(path, farmer_details_dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(farmer_details_dict, f, indent=4)
    print("Information saved to data base.")

# Load users form file if it exists
def load_farmer_registration(path):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
                return loaded_data
            
        except json.JSONDecodeError:
            print("Warning: User file is corrupted. Starting with empty data.")
            return {}
    return {}


# user = load_farmer_registration(path)

# def farmer_login():
#     phnon_no = int(input("\nEnter your phone number\nPhone number: "))
#     if phnon_no in save_farmer_registration(farmer_details_dict=)
#     pin = int(input("\nEnter your 4-digit pin below\nPin: "))



# Farmer registration
def farmer_registration():
    #Handle user registration
    user = load_farmer_registration(path)
    
    while True:
        print("\n\tYou are about to register as a Farmer.")
        farmer_phone_no = input("Enter phone number (11 digits): ").strip()
        
        if len(farmer_phone_no) != 11 or not farmer_phone_no.isdigit():
            print("Phone number must be 11 digits!")
            continue

        if farmer_phone_no in user:
            print("This number is already registered.")
            return
        break

    farmer_name = input("Enter your name: ").strip().title()

    farmer_loaction = input("Enter your location: ").strip().title()
    while True:
        farmer_pin = input("Create a 4-digit pin: ").strip()
        if len(farmer_pin) != 4 or not farmer_pin.isdigit():
            print("Pin must be 4 digits!")
            continue
        break

    user[farmer_phone_no] = {
        "Name": farmer_name,
        "Location": farmer_loaction,
        "Pin": farmer_pin
    }

    save_farmer_registration(path, user)
    print(f"Registration successful! Welcone, {farmer_name}")

    

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


