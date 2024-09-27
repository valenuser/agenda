from persona import Persona
from contacts import contacts
from verifications import verify_contact



def add_contact(user):
    while True:
        name_contact = input("New contact's name: ")
        
        if len(name_contact) > 0 or name_contact != ' ' or name_contact.find(' ') == -1:

            if verify_contact(name_contact):

                print("The name already exists.")

            else:

                break

        else:

            print("Contact names cannot have spaces")

    while True:

        try:

            number_contact = int(input("New contact's number: "))

            if name_contact > 9 or number_contact < 9:

                print("Contact number must be a number with 9 caracters.")

            break

        except Exception as e:

            print("Contact number must be 9 caracters long.")

    response = user.add_contact(name_contact,number_contact)

    if response:

        return 'Contact added succesfully.'
    
    else:

        return 'Error adding new contact.'
    


""" def edit_contact """