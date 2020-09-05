import csv

# Create people class

class People:
    """ Create People class with three attributes, name, phone_number, and address"""

    def __init__(self, name, phone_number, address):

        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.people_contact = []


    def __str__(self):

        return self.name + "'s phone number and address are " + self.phone_number + self.address


# open the file & csv.reader

with open("/Users/heejeonglim/PycharmProjects/Contact_Class/contact.csv", "r") as files:
    reader = csv.reader(files, delimiter=',')
    header = next(reader, None)

# reformat it into a python object list of lists

    data_lines = list(reader)

    # for line in data_lines:
    #     print(line)

    all_names = []

    for line in data_lines:
        all_names.append(line[0])

# print(all_names)
#     contact_list = []
#
#     for i in reader:
#         contact_list.append(i)
#
# print(contact_list)
#
# user_input = input("Who do you want to contact?: ").title()
#
# if user_input in contact_list:
#     print(contact_list)
#     print('Yes')
#
#
# # Write csv file
#
with open("/Users/heejeonglim/PycharmProjects/Contact_Class/contact.csv", mode="w") as files:
    writer = csv.writer(files, delimiter=',')
    writer.writerow(['Sebastian Thurn', '555-000-999', '000 Heave Cir. Menlo Park CA'])

files.close()

with open("/Users/heejeonglim/PycharmProjects/Contact_Class/contact.csv", mode="a") as files:
    writer = csv.writer(files, delimiter=',')
    writer.writerow(['Sooo Thurn', '111-000-999', '000 Uili Cir. Menlo Park CA'])

files.close()

