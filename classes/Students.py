from classes import DbMongo, Careers
from classes import data

class Students:

    def __init__(self, numero_cuenta,nombre_completo,cursos_aprobados,cursos_reprobados,edad, carrera, id = ""):
        self.numero_cuenta = numero_cuenta
        self.nombre_completo = nombre_completo
        self.cursos_aprobados = cursos_aprobados
        self.cursos_reprobados = cursos_reprobados
        self.edad = edad
        self.carrera = carrera
        self.__id = id
        self.__collection = "student"

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
        collection = db["student"]
        students = collection.find()

        list_students= []
        for e in students:
            temp_student = Students(
                e["numero_cuenta"]
                , e["nombre_completo"]
                , e["cursos_aprobados"]
                , e["cursos_reprobados"]
                , e["edad"]
                , e["carrera"]
                , e["_id"] 
            )

            list_students.append(temp_student)
        return list_students
    
    @staticmethod
    def delete_all(db):
        lista_e = Students.get_list(db)
        for e in lista_e:
            e.delete(db)
    @staticmethod
    def print_full_report_long_path(db):
        collection = db["student"]

        for e in collection.find():
            r = { 
                "numero_cuenta" : e["numero_cuenta"]
                , "nombre_completo": e["nombre_completo"] 
                , "cursos_aprobados": e["cursos_aprobados"] 
                , "cursos_reprobado": e["cursos_reprobado"] 
                , "edad": e["edad"] 
                , "carrera": e["carrera"] 
                , "tipo": Careers.get_one(db, e["tipo_estudiante"] ).tipo
            }
            print(r)

    @staticmethod
    def print_full_report_short_path(db):
        collection = db["student"]

        result = collection.aggregate([
            {
                '$lookup': {
                    'from': "tipo_estudiante"
                    , 'localField': "tipo_estudiante"
                    , "foreignField": "_id"
                    , "as": "te"
                }
            },{
                '$project': {
                    'nombre': 1
                    , 'telefono': 1
                    , 'te.tipo': 1
                }  
            }
        ])

        for d in result:
            print(d)


        