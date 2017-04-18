from Person import Person

class Student(Person):

    def __init__(self, name, surname, student_id):
        super(Student, self).__init__(name, surname)
        self.__student_id = student_id #Student id is private to the student
        self.course_units = []
        self.__accesslevel = "Limited Access"

    def enrol(self, course):
        self.course_units.append(course)

    def show_course_units(self):
        courses = (",").join(self.course_units)
        print "{0} enrolled for {1}".format(self.name, courses)

    def setStudentId(self, id):
        self.__student_id = id

    def getStudentId(self, id):
        print self.__student_id

    # Ploymorphism Subclass define different behavior
    def get_access_level(self):
        return self.__accesslevel