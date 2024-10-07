# Contact class to store contact information

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print("Contact_name :",contact.name ,",","Phone_number :"  ,contact.phone_number)

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone_number]
        return results

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                return
        print("Contact not found")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return
        print("Contact not found")

contact_manager = ContactManager()

while True:
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_manager.add_contact(name, phone_number, email, address)
    elif choice == "2":
        contact_manager.view_contact_list()
    elif choice == "3":
        Update = input("Enter search name: ")
        results = contact_manager.search_contact(Update)
        for result in results:
            print(result.name,":" ,result.phone_number)
    elif choice == "4":
        name = input("Enter name: ")
        new_phone_number = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")
        contact_manager.update_contact(name, new_phone_number, new_email, new_address)
    elif choice == "5":
        name = input("Enter name: ")
        contact_manager.delete_contact(name)
    elif choice == "6":
        break
    else:
        print("Invalid choice")