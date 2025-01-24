# Contact Management System

# Using a dictionary to store contact details with the name as the key
contacts = {}

# Function to add a new contact
def add_contact(name, phone, email):
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = (phone, email)
        print("Contact added.")

# Function to retrieve a contact
def get_contact(name):
    if name in contacts:
        return f"Name: {name}, Phone: {contacts[name][0]}, Email: {contacts[name][1]}"
    else:
        return "Contact not found."

# Function to update a contact
def update_contact(name, phone, email):
    if name in contacts:
        contacts[name] = (phone, email)
        print("Contact updated.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Example usage
add_contact("John Doe", "123-456-7890", "john.doe@example.com")
print(get_contact("John Doe"))
update_contact("John Doe", "987-654-3210", "new.john.doe@example.com")
print(get_contact("John Doe"))
delete_contact("John Doe")
print(get_contact("John Doe"))
