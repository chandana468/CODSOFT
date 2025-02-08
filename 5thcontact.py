import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load existing contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts = load_contacts()
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("No contacts found.")

# Search for a contact
def search_contact():
    search_term = input("Enter Name or Phone Number to search: ").strip()
    contacts = load_contacts()
    found = False

    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details["Phone"]:
            print("\n--- Contact Found ---")
            print(f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            found = True
            break

    if not found:
        print("Contact not found.")

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()

    if name in contacts:
        print("\nEnter new details (leave blank to keep existing values):")
        phone = input(f"New Phone ({contacts[name]['Phone']}): ").strip() or contacts[name]['Phone']
        email = input(f"New Email ({contacts[name]['Email']}): ").strip() or contacts[name]['Email']
        address = input(f"New Address ({contacts[name]['Address']}): ").strip() or contacts[name]['Address']

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu
def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
