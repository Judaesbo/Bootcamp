import datetime
import operator

class Contact():
    def __init__ (self, name, last_name, age, email, phone_dict):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone_dict = phone_dict
        self.created = datetime.datetime.now()
        
class  Contact_list(Contact):
    def __init__(self, name, last_name, age, email, phone_dict, v):
        
    
def update_contact(l, i, name, last_name, age, email, phone_dict):
    l[i]=Contact(name, last_name, age, email, phone_dict)


def add_contact(l, name, last_name, age, email, phone_dict):
    l.append(Contact(name, last_name, age, email, phone_dict))

def hide_contact(l, name, last_name):
    [a for a in l  if (a.name =! name and (a.last_name =! last_name))]
    return a