class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self):
        ## Do something to create careers on your mongodb collection using __data
        print(self.__data.carrera)
        return self.create_careers()
    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        return self.create_courses()
    def create_students(self):
        ## Do something to create students on your mongodb collection using __data
        return self.create_students()
    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        return self.create_enrollments()