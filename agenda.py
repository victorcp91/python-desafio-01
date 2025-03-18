from utils import is_valid_entry

agenda = []

options = {
    "1": "All contacts",
    "2": "Add contact",
    "3": "Edit contact",
    "4": "Set/unset favorite",
    "5": "Only favorites",
    "6": "Erase contact",
    "7": "Exit"
}

def add_contact():
    name = input("Enter a contact name:\n")
    while not is_valid_entry(name, "name"):
        name = input("Invalid input! Enter a valid name:\n")

    email = input("Enter the contact email:\n")
    while not is_valid_entry(email, "email"):
        email = input("Invalid input! Enter a valid email:\n")

    phone = input("Enter the contact phone number:\n")
    while not is_valid_entry(phone, "phone"):
        phone = input("Invalid input! Enter a valid phone number:\n")

    favorite = input("Contact is a favorite? (S/N):\n")
    while not is_valid_entry(favorite, "favorite"):
        favorite = input("Invalid input! Valid options 'S' or 'N':\n")

    agenda.append({
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": favorite.lower() == "s"
    })
    print("Contact added successfully!")

def list_contacts():
    if not agenda:
        print("No contacts found.")
        return

    for index, contact in enumerate(agenda, start=1):
        favorite = "x" if contact["favorite"] else " "
        print(f"""
        {index}. {contact['name']}      favorite: [{favorite}]
        phone number: {contact['phone']}
        email: {contact['email']}\n""")

def edit_contact():
    list_contacts()
    contact_number = input("Enter the contact number you want to edit:\n")
    if not contact_number.isdigit() or int(contact_number) > len(agenda):
        print("Invalid number.")
        return

    real_index = int(contact_number) - 1
    update_data_type = input("""
    What data you want to update?
    1. Name
    2. Phone number
    3. Email\n""")

    if update_data_type == "1":
        name = input("Enter a new name:\n")
        while not is_valid_entry(name, "name"):
            name = input("Invalid input! Enter a valid name:\n")
        agenda[real_index]["name"] = name

    elif update_data_type == "2":
        phone = input("Enter a new phone number:\n")
        while not is_valid_entry(phone, "phone"):
            phone = input("Invalid input! Enter a valid phone number:\n")
        agenda[real_index]["phone"] = phone

    elif update_data_type == "3":
        email = input("Enter a new email:\n")
        while not is_valid_entry(email, "email"):
            email = input("Invalid input! Enter a valid email:\n")
        agenda[real_index]["email"] = email
    else:
        print("Invalid option.")
        return
    print("Contact edited successfully!")

def set_unset_favorite():
    list_contacts()
    contact_number = input("Enter the contact number you want to set/unset as favorite:\n")
    if not contact_number.isdigit() or int(contact_number) > len(agenda):
        print("Invalid number.")
        return

    real_index = int(contact_number) - 1
    agenda[real_index]["favorite"] = not agenda[real_index]["favorite"]
    print("Favorite status updated successfully!")

def list_favorite_contacts():
    favorite_contacts = [contact for contact in agenda if contact["favorite"]]
    if not favorite_contacts:
        print("No favorite contacts found.")
        return

    for index, contact in enumerate(favorite_contacts, start=1):
        print(f"""
        {index}. {contact['name']}]
        phone number: {contact['phone']}
        email: {contact['email']}\n""")

def erase_contact():
    list_contacts()
    contact_number = input("Enter the contact number you want to erase:\n")
    if not contact_number.isdigit() or int(contact_number) > len(agenda):
        print("Invalid number.")
        return
    del agenda[int(contact_number) - 1]
    print("Contact erased successfully!")

# Main menu
def main_menu():
    while True:
        print("\nAgenda:")
        for key, value in options.items():
            print(f"{key}. {value}")

        selected_option = input("\nSelect an action:\n")

        if selected_option == "1":
            list_contacts()
        elif selected_option == "2":
            add_contact()
        elif selected_option == "3":
            edit_contact()
        elif selected_option == "4":
            set_unset_favorite()
        elif selected_option == "5":
            list_favorite_contacts()
        elif selected_option == "6":
            erase_contact()
        elif selected_option == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

main_menu()