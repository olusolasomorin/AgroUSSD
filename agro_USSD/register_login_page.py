"""This is an AgroUSSD for NIgerian farmers and buyers with basic mobile phones to have access to real-time market prices, connect farmers directly to buyers and provide basic crop management information.
This simulated USSD will in the long run cut middlemen exploitation down to 90% and takes away the constraint caused by distance for farmers in getting their produce to urban markets.
"""


# Using TRY-EXCEPT for IndexErrors and TRY-EXCEPT-FINALLY
# Ask user to input USSD
while True:
    ussd = input("Enter the USSD code: ")
    if ussd == "*967#":

        print("\nFor English, Press 1")
        print("Fun ede Yoruba, te 2")
        print("Don harshen Hausa, danna 3")
        print("Maka asusu igbo, pia 4")
        print("For Pidgin, press 5\n")

    lang_choice = input("Please enter an option: ")
    if lang_choice == "1":
            print("\nWelcome to Nigeria DIgital Agro-marketplace\n ")
            print("1. Register")
            print("2. Login")
            print("3. More information")
            print("4. Contact info")
            print("5. Exit")
    option = input("\nPlease select an option: ")
    if option == "5":
         print("Goodbye!\nThank you for using our service.")
         break
    if option == "1":
                print("Select the right option")
                print("Are you: ")
                print("1. Farmer")
                print("2. Buyer")
                register = input("Select an option: ")
                if register == "1":
                       farmers_details = {}
                       print("Fill in your information correctly: ")
                       name = input("Enter your full name: ").upper()
                       name = name.split()
                       age = int(input("Enter your age: "))
                       gender = input("Are you a female or a male: ").title()
                       state = input("Enter your state of residence: ").title()
                       local_govt_area = input("Enter your LGA: ").title()
                       city_or_town_or_Village = input("Which city/town/village is your farm located?: ")

                       small_size = "Below 2 hectares"
                       medium_size = "2 hectares - 10 hectares"
                       Large_size = "Above 10 hectares"
                       farm_size = [small_size, medium_size, Large_size]

                       farm_size = input(f"Enter your farm size{farm_size}: ").title()
                       phone_no = input("Enter your phone no: ")

                       if len(phone_no) == 10 and phone_no.isdigit(): 
                              print(f"Your phone number {phone_no} should be used as your user_Id")

                       elif len(phone_no) < 10:
                              print(f"Your phone number is incomplete")

                       else:
                              print("Invalid input")
                       
                       user_Id = input("Enter your phone number as your user ID: ")
                       user_Id_confirmation = input("Confirm your user_Id: ")
                       pin = input("Enter a four digit nuber as your pin: ")
                       confirm_pin = input("Confirm your pin: ")

                       if user_Id == user_Id_confirmation and phone_no == pin == confirm_pin:
                             print(f"\nRegistration successful!")
                farmers_details = {"Name": name, "Age": age, "Gender": gender, "State": state, "LGA": local_govt_area, "Farm Location": city_or_town_or_Village, "Farm size": farm_size, "Phone Number/UserID": phone_no, "PIN": "****"}
                print(f"{farmers_details}")

                
                pass
    
                register = input("Select an option: ")
                if register == "2":
                       buyers_details = {}
                       print("Fill in your information correctly: ")
                       name = input("Enter your full name: ").upper()
                       name = name.split()
                       age = int(input("Enter your age: "))
                       gender = input("Are you a female or a male: ").title()
                       state = input("Enter your state of residence: ").title()
                       local_govt_area = input("Enter your LGA: ").title()
                       city_or_town_or_Village = input("Which city/town/village is your farm located?: ")
                       phone_no = input("Enter your phone no: ")

                       if len(phone_no) == 10 and phone_no.isdigit(): 
                              print(f"Your phone number {phone_no} should be used as your user_Id")

                       elif len(phone_no) < 10:
                              print(f"Your phone number is incomplete")

                       else:
                              print("Invalid input")
                       
                       user_Id = input("Enter your phone number as your user ID: ")
                       user_Id_confirmation = input("Confirm your user_Id: ")
                       pin = input("Enter a four digit nuber as your pin: ")
                       confirm_pin = input("Confirm your pin: ")

                       if user_Id == user_Id_confirmation and phone_no == pin == confirm_pin:
                             print(f"\nRegistration successful!")
                farmers_details = {"Name": name, "Age": age, "Gender": gender, "State": state, "LGA": local_govt_area, "Farm size": farm_size, "Phone Number/UserID": phone_no, "PIN": "****"}
                print(f"{buyers_details}")
                break
        
    if option == 2:
           UserID = input("Enter your userID: ")
           pin = input("Enter your four digit pin: ")
           

                            


                