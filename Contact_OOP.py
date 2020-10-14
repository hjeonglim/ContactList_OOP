import csv


# Create a person class with attributes including name, phone_number, address
class Person:

    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Address: {self.address}"


def contact():
    """Create a contact function that put content to the list after reading info from csv file"""
    contact_list = []

    with open("/Users/heejeonglim/PycharmProjects/Contact_OOP/contact.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)

        for r in reader:
            person = Person(r[0], r[1], r[2])
            contact_list.append(person)

    return contact_list


contact_book = contact()


def print_contact(ct_list, print_num=False):
    for i, contact in enumerate(ct_list, 1):
        if print_num:
            print(f'{i}. {contact}')
        else:
            print(contact)


def command_list():
    while True:
        user_input = input("Select command 'l' for list, 'x' for exit, and : 'd' for delete from the list").lower()

        if user_input == "l":
            # print_contact(contact_book)
            print_contact(contact_book)

        elif user_input == "d":
            print_contact(contact_book, print_num=True)

            # Ask which contact list to delete
            delete_input = int(input(f"Which one do you want to delete? 1-{len(contact_book)}"))
            contact_book.pop(delete_input-1)
            print_contact(contact_book, print_num=True)

        elif user_input == "x":
            break


command_list()


class ContactBook:
    def print(self):


    def delete(self):

    def add(self):

    def save(self):



