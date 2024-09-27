from contacts import agenda

class Persona:

    def __init__(self,name,number):
        self.name = name
        self.number = number

    def add_contact(self,name,number):
        
        agenda[name] = number

        print(agenda)

        return True

    def delete_contact(self,name):

        agenda[self.name].pop(name)

    def edit_contact(self,name,number):

        agenda[self.name][name] = number
