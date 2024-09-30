from contacts import contacts,phones

def verify_contact(name):

    if contacts.get(name) != None:

        return True
    
    else:
    
        return False



def verify_number(number):
    try:
        if number in phones:

            return False
    
    except Exception as e:

        return True