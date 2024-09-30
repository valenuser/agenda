from persona import Persona
from contacts import contacts, phones
from verifications import verify_contact,verify_number



def change_phone(old_number, new_number):

    try:

        index_old_number = phones.index(old_number)

        phones[index_old_number] = new_number

        return True
    
    except Exception as e:

        return False


def add_contact(user):
    while True:
        name_contact = input("New contact's name: ")
        
        if len(name_contact) > 0 or name_contact != ' ' or name_contact.find(' ') == -1:

            if verify_contact(name_contact):

                print("The name already exists.")

            else:
                    break


        else:

            print("Contact names cannot have spaces.")

    while True:

        try:

            number_contact = int(input("New contact's number: "))

            if len(str(number_contact)) != 9:

                print("Contact number must be 9 caracters long.")

            elif verify_number(number_contact) == None:
                        
                break
                    
            else:

                print("Number already exists.")

        except Exception as e:

            print("Contact number must be 9 caracters long.")
    
    phones.append(number_contact)
    response = user.add_contact(name_contact,number_contact)

    if response:

        return 'Contact added succesfully.'
    
    else:

        return 'Error adding new contact.'
    


def edit_contact(user):
    
        while True:

            edit_name_contact = input("Contact's name: ")

            if verify_contact(edit_name_contact):

                    break

            else:

                print("The contact is not registered.")


        while True:
             
            try:
                                
                edit_number_contact = int(input("New contact's number: "))

                if len(str(edit_number_contact)) != 9:

                    print("Contact number must be 9 caracters long.")

                elif verify_number(edit_number_contact) == None:
                                        
                    break
                                    
                else:

                    print("Number already exists.")
                
            
            except Exception as e:
                 
                print("Contact number must be 9 caracters long.")


        old_number = contacts[edit_name_contact]
        
        change_phone(old_number,edit_number_contact)

        response = user.edit_contact(edit_name_contact,edit_number_contact)

        if response:
            
            return "Contact changed succesfully."

        else:
            
            return 'Error changing the contact, try again later.'
        


def delete_contact(user):
        while True:

            delete_name_contact = input("Contact's name: ")

            if verify_contact(delete_name_contact):

                    break

            else:

                print("The contact is not registered.")

        
        phone = contacts[delete_name_contact]

        phones.remove(phone)

        
        response = user.delete_contact(delete_name_contact)

        if response:
        
             return "The contact has been deleted."
        
        else:
             
             return "The contact hasn't been deleted, try again later."