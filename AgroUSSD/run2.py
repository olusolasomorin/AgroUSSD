from A_SIC.interface import main_menu


try:
    while True:
        ussd_code = input("Dial *976#: ")
        if ussd_code != "*976#":
            continue
        else:
            break

    while True:
        main_menu.display()
        choice = int(input("Enter choice: "))
        if choice == 1:
            main_menu.handle_input(choice)

        elif choice == 2:
             main_menu.handle_input(choice)
except Exception as e:
    print("Error as", e)