# Lists to store contacts
names = []
numbers = []
emails = []
addresses = []

def add_contact(n, no, mail, add):
    names.append(n)
    numbers.append(no)
    emails.append(mail)
    addresses.append(add)

def view_contacts():
    for i in range(len(names)):
        print(f"Name: {names[i]}, Contact No.: {numbers[i]}, Email: {emails[i]}, Address: {addresses[i]}")
        print("")

def search_by_name(n):
    for i, name in enumerate(names):
        if name == n:
            print_contact_info(i)
            break
    else:
        print("Contact not found.")

def search_by_number(no):
    for i, number in enumerate(numbers):
        if number == no:
            print_contact_info(i)
            break
    else:
        print("Contact not found.")

def print_contact_info(i):
    print(f"Name: {names[i]}, Contact No.: {numbers[i]}, Email: {emails[i]}, Address: {addresses[i]}")
    print("")

def update_contact():
    view_contacts()
    temp = input("Enter the name of the person whose details you wish to change: ")
    for i, name in enumerate(names):
        if name == temp:
            print("1. Update Name")
            print("2. Update Number")
            print("3. Update Email")
            print("4. Update Address")
            choice = int(input("Please make a choice: "))
            if choice == 1:
                n = input("Enter the new name: ")
                names[i] = n
            elif choice == 2:
                no = input("Enter the new contact number to update: ")
                numbers[i] = no
            elif choice == 3:
                mail = input("Enter the new email to update: ")
                emails[i] = mail
            elif choice == 4:
                add = input("Enter the new address to update: ")
                addresses[i] = add
            print("Contact updated.")
            break
    else:
        print("Contact not found.")

def delete_contact():
    view_contacts()
    temp = input("Enter the name of the person whose details you wish to delete: ")
    for i, name in enumerate(names):
        if name == temp:
            names.pop(i)
            numbers.pop(i)
            emails.pop(i)
            addresses.pop(i)
            print("Contact deleted.")
            break
    else:
        print("Contact not found.")

print("Welcome to the contact book!")
while True:
    print("1. Add a Contact")
    print("2. View Contacts")
    print("3. Search a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = input("Please enter the name: ")
        no = input("Please enter the phone number: ")
        mail = input("Please enter the email: ")
        add = input("Please enter the address: ")
        add_contact(n, no, mail, add)
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_type = int(input("Do you want to search by name(1) or number(2)? "))
        if search_type == 1:
            n = input("Please enter the name to search with: ")
            search_by_name(n)
        elif search_type == 2:
            no = input("Please enter the number to search with: ")
            search_by_number(no)
        else:
            print("Invalid choice.")
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        break
    else:
        print("Invalid Choice!!!")
