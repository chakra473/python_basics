import os
import json


class AddressBook(object):
    def __init__(self, name=None, address=None, email=None, phone=None):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.contacts = {}
        self.filename = 'address_book_file.json'

    def __str__(self):
        return '[Name: {0} | Address: {1} | Email: {2} | Phone: {3}]'.format(self.name,
                                                                             self.address, self.email, self.phone)

    def __repr__(self):
        return '[Name: {0} | Address: {1} | Email: {2} | Phone: {3}]'.format(self.name,
                                                                             self.address, self.email, self.phone)

    # Adding details provided by the user in our Address Book
    def add_contacts(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                my_address_book = open(self.filename, 'r')
                data = json.load(my_address_book)
                my_address_book.close()
            else:
                my_address_book = open(self.filename, 'w')
                data = {}

            contact = self.get_details_from_user()
            data[contact['Name']] = contact
            my_address_book = open(self.filename, 'w')
            json.dump(data, my_address_book)
            my_address_book.close()
            print('Contact Added Successfully!')
        except Exception as e:
            print('There was an error! Contact was not added.')
            print(e)
        finally:
            my_address_book.close()

    # Getting the details from the user to adding the Address Book
    def get_details_from_user(self):

        self.contacts['Name'] = str(input('Enter Contact\'s Full Name: '))
        self.contacts['Address'] = str(input('Enter Contact\'s Address: '))
        self.contacts['Email'] = str(input('Enter Contact\'s Email Address: '))
        self.contacts['Phone'] = int(input('Enter Contact\'s Phone Number: '))
        return self.contacts

    # To display ALL the contact in our Address Book
    def display_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            my_address_book = open(self.filename, 'r')
            data = json.load(my_address_book)
            my_address_book.close()
            if data:
                for records in data.values():
                    print(records)
            my_address_book.close()
        else:
            print('No Record in database.')

    # To search for a specific contact in our Address Book
    def search_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            my_address_book = open(self.filename, 'r')
            data = json.load(my_address_book)
            my_address_book.close()
            try:
                contact_to_search = input('Enter the name of the contact to search: ')
                counter = 0
                for contact in data.values():
                    if contact_to_search in contact['Name']:
                        print(data[contact['Name']])
                        counter += 1
                if counter == 0:
                    print('No record found whose name is:', contact_to_search)
            except Exception as ex:
                print('Error occurred!', ex)
        else:
            print('No Record in database.')

    # For modifying contacts
    def modify_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            my_address_book = open(self.filename, 'r')
            data = json.load(my_address_book)
            my_address_book.close()
            try:
                contact_to_modify = input('Enter the name of the contact to modify (Only enter full name): ')
                # Search for the record to update
                for contact in data.values():
                    if contact_to_modify == contact['Name']:
                        contact = data[contact_to_modify]
                        break
                option = int(input('1. To modify name, 2. To modify address, 3. To modify email, 4. To modify phone: '))
                if option == 1:
                    contact['Name'] = input('Enter Name to modify: ')
                    del data[contact_to_modify]
                    data[contact['Name']] = contact
                    print('Successful')
                elif option == 2:
                    contact['Address'] = input('Enter Address to modify: ')
                    del data[contact_to_modify]
                    data[contact_to_modify] = contact
                    print('Successful')
                elif option == 3:
                    contact['Email'] = input('Enter Email to modify: ')
                    del data[contact_to_modify]
                    data[contact_to_modify] = contact
                    print('Successful')
                elif option == 4:
                    contact['Phone'] = input('Enter Phone to modify: ')
                    del data[contact_to_modify]
                    data[contact_to_modify] = contact
                    print('Successful')
                else:
                    print('Incorrect option selected.')
            except Exception as e:
                print('Error occurred. No such record found. Try Again!', e)
            finally:
                my_address_book = open(self.filename, 'w')
                json.dump(data, my_address_book)
                my_address_book.close()
        else:
            print('No Record in database.')


if __name__ == '__main__':
    myBook = AddressBook()
    print("1 to Add contact, \n2 to display contact"
          "\n3 For Searching a Contact \n4. For Modifying a Contact")
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            myBook.add_contacts()
        elif choice == 2:
            myBook.display_contacts()
        elif choice == 3:
            myBook.search_contacts()
        elif choice == 4:
            myBook.modify_contacts()
