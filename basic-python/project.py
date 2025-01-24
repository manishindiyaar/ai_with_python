
contacts ={} #dictionary

def add_contact(name, phone , email):
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name]=(phone, email)
        print("Contact added.")

def get_contact(name):
    if name in contacts:
        return f"Name: {name}, Phone: {contacts[name][0]}, Email: {contacts[name][1]}"
    else:
        return "Contact not found."



# Testing add_contact()

# i want to call this function 3 times
# add_contact("Manish Doe", "923-456-7890", "mindiyaa@bladex.com")
# add_contact("Jane Smith", "123-456-7890", "jane.smith@example.com")
# add_contact("John Doe", "987-654-3210", "john.doe@example.com")
# add_contact = add_contact("Manish Doe", "923-456-7890", " mindiyaa@bladex.com")

# print(contacts)     

# Testing get_contact()
# get_contact = get_contact("Manish Doe")
# print(get_contact)


def update_contact(name, phone, email):
    if name in contacts:
        contacts[name]=(phone, email)
        print("Contact updated.")
    else:
        print("Contact not found.")



def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n1. Add Contact")
    print("2. Get Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == '2':
        name = input("Enter name: ")
        print(get_contact(name))
    elif choice == '3':
        name = input("Enter name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        update_contact(name, phone, email)
    elif choice == '4':
        name = input("Enter name: ")
        delete_contact(name)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")