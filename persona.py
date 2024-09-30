from contacts import contacts

class Persona:

    def __init__(self,name,number):
        self.name = name
        self.number = number

    def add_contact(self,name,number):
        
        contacts[name] = number

        print(contacts)

        return True

    def delete_contact(self,name):

        contacts.pop(name)

        return True

    def edit_contact(self,name,number):

        contacts[name] = number

        return True
