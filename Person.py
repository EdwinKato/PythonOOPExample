class Person(object):
    person_count = 0

    def __init__(self, name, surname):
        #name and surname are public
        self.name = name
        self.surname = surname
        self._increment_no_of_people()

    def display_no_of_people(self):
        print "The number of people in the school is %d" %Person.person_count

    #Protected method
    def _increment_no_of_people(self):
        Person.person_count += 1

    def get_access_level(self):
        raise NotImplementedError("Subclass must implement abstract method")