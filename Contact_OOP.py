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

    with open ("/Users/heejeonglim/PycharmProjects/Contact_Class/contact.csv", "r") as file:
        reader = csv.reader(file, delimiter = ",")
        next(reader, None)

        for r in reader:
            person = Person(r[0], r[1], r[2])
            contact_list.append(person)

    return contact_list


contact_book = contact()


def command_list():

    while True:
        user_input = input("Select command 'l' for list, 'x' for exit, and : 'd' for delete from the list").lower()

        if user_input == "l":
            for contact in contact_book:
                print(contact)
        elif user_input == "d":
            for i, contact in enumerate(contact_book, 1):
                print(f'{i}. {contact}')

            # Ask which contact list to delete
            delete_input = str(input("Which one do you want to delete? "))

            writer = csv.writer(open("/Users/heejeonglim/PycharmProjects/Contact_Class/contact.csv", 'w'))

            for line in contact_book:
                if delete_input in line:
                    writer.writerow(line)

            writer.close()

        elif user_input == "x":
            break

command_list()

# def print_contact():
#     """Create a command to execute or exit"""
#
#     user_input = ""
#
#     while user_input != "Y":
#         user_input = input("Do you want to see the contact list? Y or N").upper()
#
#         if user_input == "Y":
#             for contact in contact_book:
#                 print(contact)
#         else:
#             exit()
#
# print_contact()
