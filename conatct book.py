import os
from colorama import Fore, Style, init

init(autoreset=True)

names = []
numbers = []

def clear_screen():
    os.system('cls')

def store_contact():
    clear_screen()
    name = input(Fore.CYAN + "Enter Name:: ").upper()
    number = int(input(Fore.CYAN + "Enter Num:: "))
    names.append(name)
    numbers.append(number)
    print(Fore.GREEN + "Contact added successfully!")

def search_contact():
    clear_screen()
    print(Fore.YELLOW + "Enter \nA for search from name\nB for search from number: ")
    choice = input(Fore.CYAN + "Choice: ").upper()
    if choice == 'A':
        name = input(Fore.CYAN + "Enter Name:: ").upper()
        if name in names:
            print(Fore.GREEN + "Number:", numbers[names.index(name)])
        else:
            print(Fore.RED + "Name not found.")
    elif choice == 'B':
        num = int(input(Fore.CYAN + "Enter Number:: "))
        if num in numbers:
            print(Fore.GREEN + "Name:", names[numbers.index(num)])
        else:
            print(Fore.RED + "Number not found.")
    else:
        print(Fore.RED + "Invalid choice.")

def update_contact():
    clear_screen()
    print(Fore.YELLOW + "Enter \nA for update number\nB for update name")
    choice = input(Fore.CYAN + "Choice: ").upper()
    if choice == 'A':
        clear_screen()
        print(Fore.YELLOW + "Enter \nA for update number from name\nB for update number from number")
        choice = input(Fore.CYAN + "Choice: ").upper()
        if choice == 'A':
            clear_screen()
            name = input(Fore.CYAN + "Enter Name:: ").upper()
            if name in names:
                print(Fore.GREEN + "Current Number:", numbers[names.index(name)])
                new_number = int(input(Fore.CYAN + "Enter New Num:: "))
                numbers[names.index(name)] = new_number
                print(Fore.GREEN + "Contact updated successfully!")
            else:
                print(Fore.RED + "Name not found.")
        elif choice == 'B':
            num = int(input(Fore.CYAN + "Enter Number:: "))
            if num in numbers:
                print(Fore.GREEN + "Current Name:", names[numbers.index(num)])
                new_number = int(input(Fore.CYAN + "Enter New Number:: "))
                numbers[numbers.index(num)] = new_number
                print(Fore.GREEN + "Contact updated successfully!")
            else:
                print(Fore.RED + "Number not found.")
        else:
            print(Fore.RED + "Invalid Choice")
    
    elif choice == 'B':
        clear_screen()
        print(Fore.YELLOW + "Enter \nA for update name from name\nB for update name from number: ")
        choice = input(Fore.CYAN + "Choice: ").upper()
        if choice == 'A':
            name = input(Fore.CYAN + "Enter Name:: ").upper()
            if name in names:
                print(Fore.GREEN + "Current Number:", numbers[names.index(name)])
                new_name = input(Fore.CYAN + "Enter New Name:: ").upper()
                names[names.index(name)] = new_name
                print(Fore.GREEN + "Contact updated successfully!")
            else:
                print(Fore.RED + "Name not found.")
        elif choice == 'B':
            num = int(input(Fore.CYAN + "Enter Number:: "))
            if num in numbers:
                print(Fore.GREEN + "Current Name:", names[numbers.index(num)])
                new_name = input(Fore.CYAN + "Enter New Name:: ").upper()
                names[numbers.index(num)] = new_name
                print(Fore.GREEN + "Contact updated successfully!")
            else:
                print(Fore.RED + "Number not found.")
        else:
            print(Fore.RED + "Invalid Choice")
    else:
        print(Fore.RED + "Invalid Choice")

def delete_contact():
    clear_screen()
    print(Fore.YELLOW + "Enter \nA for delete contact from name\nB for delete contact from number")
    choice = input(Fore.CYAN + "Choice: ").upper()
    if choice == 'A':
        name = input(Fore.CYAN + "Enter Name: ").upper()
        if name in names:
            index = names.index(name)
            print(Fore.RED + "WARNING: You are about to delete the contact. This action cannot be undone.")
            confirm = input(Fore.RED + "Do you want to proceed? (Y/N): ").upper()
            if confirm == 'Y':
                del names[index]
                del numbers[index]
                print(Fore.GREEN + "Contact deleted successfully!")
            else:
                print(Fore.YELLOW + "Deletion cancelled.")
        else:
            print(Fore.RED + "Name not found.")
    elif choice == 'B':
        number = int(input(Fore.CYAN + "Enter Num:: "))
        if number in numbers:
            index = numbers.index(number)
            print(Fore.RED + "WARNING: You are about to delete the contact. This action cannot be undone.")
            confirm = input(Fore.RED + "Do you want to proceed? (Y/N): ").upper()
            if confirm == 'Y':
                del names[index]
                del numbers[index]
                print(Fore.GREEN + "Contact deleted successfully!")
            else:
                print(Fore.YELLOW + "Deletion cancelled.")
        else:
            print(Fore.RED + "Number not found.")
    else:
        print(Fore.RED + "Invalid choice.")

def show_contacts():
    clear_screen()
    if names:
        print(Fore.GREEN + "Contacts:")
        for name, number in zip(names, numbers):
            print(f"{Fore.CYAN}{name}::{number}")
    else:
        print(Fore.RED + "No contacts to display.")

def main_menu():
    while True:
        clear_screen()
        print(Fore.YELLOW + "Enter:")
        print("1 for store new contact")
        print("2 for search contact")
        print("3 for update contact")
        print("4 for delete contact")
        print("5 for show all contacts")
        print("6 for exit")
        choice = input(Fore.CYAN + "Choice: ")

        if choice == '1':
            store_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            show_contacts()
        elif choice == '6':
            print(Fore.CYAN + "Exiting the program...")
            break
        else:
            print(Fore.RED + "Invalid choice!")

        input(Fore.CYAN + "Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
