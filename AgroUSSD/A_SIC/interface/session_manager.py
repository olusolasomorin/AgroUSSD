# from .main_menu import MainMenu

# class SessionManger:
#     def __init__(self):
#         self.menu_stack = [MainMenu()]
#         self.current_user = None

#     def get_current_menu(self):
#         return self.menu_stack[-1]
    
#     def push_menu(self, menu):
#         self.menu_stack.append(menu)

#     def pop_menu(self):
#         if len(self.menu_stack) > 1:
#             self.menu_stack.pop()
#         return self.get_current_menu()
    
#     def reset_to_main(self):
#         self.menu_stack = [MainMenu()]
#         return self.get_current_menu()

# class Farmer:
#     def __init__(self, name, location, phone_number):
#         self.name = name
#         self.location = location
#         self.phone_number =phone_number
#         # self.__pin =  


#     def farmer_registration(self):
#         farmer_details_dict = {}
#         try:
#             farmer_name = input("Enter your name: ").title()
#             farmer_details_dict['Name'] = farmer_name

#             farmer_phone_no = int(input("Enter phone number: "))
#             if len(farmer_phone_no) != 11:
#                 print("Phone number must be 11 digits!")
#             else:
#                 farmer_details_dict['Phone number'] = farmer_phone_no

#             farmer_loaction = input("Enter your location: ").title()
#             farmer_details_dict['Location'] = farmer_loaction

#             farmer_pin = int(input("Create a 4 digit pin: "))
#             if len(farmer_pin) != 4:
#                 print("Pin must be 4 digits!")
#             else:
#                 farmer_details_dict['Pin'] = farmer_pin

#             return "Account successfully created!"
#         except Exception as e:
#             print("Error as", e)