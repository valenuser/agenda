from contacts import contacts

def verify_contact(name):

    keys = contacts.keys()

    names = []

    for i in keys:
        names.append(i)

    if name in names:

        return True
    
    else:
    
        return False