class Enrollments:

    def __init__(self, students, careers, id = ""):
        self.students = students
        self.careers = careers
        self.__id = id
        self.__collection = "enrollments"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def get_list(db):
        collection = db["enrollments"]
        students = collection.find()

