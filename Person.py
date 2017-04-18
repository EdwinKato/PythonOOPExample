class Person(object):
    person_count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.increment_no_of_people()

    def display_no_of_people(self):
        print "The number of people in the school is %d" %Person.person_count

    def increment_no_of_people(self):
        Person.person_count += 1