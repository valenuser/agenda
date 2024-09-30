from persona import Persona
from functions import add_contact,edit_contact,delete_contact

user =  Persona('Valentin',123456789)


while True:
        print(f'Welcome {user.name} to your contact list!\n\nOptions:\n\n1. Add contact\n2. Edit contact\n3. Search contact\n4. Delete contact\n5. Exit\n\n')
        try:
            ask = int(input('Select your option:'))

            if ask == 1:
                print(add_contact(user))
            elif ask == 2:
                print(edit_contact(user))
            elif ask == 3:
                print(add_contact(user))
            elif ask == 4:
                print(delete_contact(user))
            elif ask == 5:
                break
        except Exception as e:
            print('You must answered with numbers')



print(f"See you soon, {user.name}.")