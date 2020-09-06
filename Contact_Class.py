import csv

# Create people class


class Person:
    """ Create People class with three attributes, name, phone_number, and address"""

    def __init__(self, name, phone_number, address):

        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        # return self.name + "'s contact info is" + self.phone_number + " and " + self.address
        return f'name: {self.name}, phone: {self.phone_number}, address: {self.address}'



# person1 = Person("Charlie BBB", "222-000-0000", "000 EEEE St Sunnyvale CA")
# print(person1)
#
# person2 = Person("Yoonu", "111", "ramona")
# print(person2)
#
# people = []
# people.append(person1)
# people.append(person2)
#
# print(len(people))
#
# for p in people:
#     print('Hi! ', p)


# reformat it into a python object list of lists


def contact_book():
    contact_list = []

    # open the file & csv.reader

    with open("/Users/heejeonglim/PycharmProjects/Contact_Class/contact.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        next(reader, None)

        for r in reader:
            print(r)
            person = Person(r[0], r[1], r[2])
            contact_list.append(person)

    return contact_list


people = contact_book()

for person in people:
    print(person)

