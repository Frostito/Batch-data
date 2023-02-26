from classes import DATA, Dataprocess
from classes import Students, DbMongo, Careers, Courses, Enrollments, data
from dotenv import load_dotenv
from classes import*

def main():
    client, db = DbMongo.getDB()
    Students.delete_all(db)
    Courses.delete_all(db)
    Careers.delete_all(db)
    
    Courses("").save(db)
    Careers("").save(db)
    Enrollments("").save(db)

    dictTipos = Courses.get_dict(db)
    dictTipos = Careers.get_dict(db)

    print(dictTipos)


    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers()
    #collection.aggregate(pipeline)
    pipeline.create_students()
    pipeline.create_enrollments()
    print(DATA)
    

    Students.print_full_report_long_path(db)
    Students.print_full_report_short_path(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()

