import logging
import logging as lg
lg.basicConfig(filename="oops.log",level=logging.DEBUG,format=("%(levelname)s %(asctime)s %(message)s"))
class Ineuron:
    logging.info("class constructer is formed")

    def __init__(self, stdnt_name, class_type, batchno, no_courses, yob):
        self.stdnt_name = stdnt_name
        self.class_type = class_type
        self.batchno = batchno
        self.no_courses = no_courses
        self.yob = yob

    def age(self, current_year):
        try:
            logging.info("will return age")
            return f"{self.stdnt_name}",current_year-self.yob
        except Exception as e:
            logging.error(e)

person1 = Ineuron("SUNNY","FULLSTACK",15,5,1995)
print(person1.age(2022))

#MULTILEVEL INHERITANCE


class Student(Ineuron):
    logging.info("inheriting Ineuron class in Student Class")
    try:
        def name_ofcoarse(self, name, batchno):
            logging.info("constructer of student class")

            if batchno == 12:
                return "DATA SCIENCE"
            elif batchno == 13:
                return "DATA ANALYST"
            elif batchno == 14:
                return "MACHINE LEARNING"
            elif batchno == 15:
                return "MY SQL"
            else:
                return "no such batch"
    except Exception as e:
        logging.error(e)

person2 = Student("RAHUL","QUIZZ",16,3,1991)
S = person2.name_ofcoarse("RAHUL",14)
print(S)

#MULTIPLE INHERITANCE

class Info(Student,Ineuron):
    logging.info(("inheriting Student class and Ineuron Class"))

    def details(self):
        try:
            logging.info("will return details of the student")
            return self.stdnt_name,self.batchno,self.no_courses,self.yob
        except Exception as e:
            logging.error(e)

person3 = Info("ROHAN","CRASH COARSE",18,5,1992)
print(person3.age(2023))
print((person3.name_ofcoarse("ROHAN",20)))

print(person3.details())








