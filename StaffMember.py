from Person import Person

class StaffMember(Person):

    def __init__(self, name, surname):
        super(StaffMember, self).__init__(name, surname)
        self.courses_taught = []

    # Ploymorphism Subclass define different behavior
    def get_access_level(self):
        return "Full access"

    def add_course(self, course):
        self.courses_taught.append(course)

    def show_courses_taught(self):
        courses = (",").join(self.courses_taught)
        print "{0} teaches {1}".format(self.name, courses)