# 10 examples on encaptulations

import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
logging.debug('showing the debug error in givan object')
logging.info('shows error in givan class and object')

class ineuron1:
    def __init__(self,course1,batch):
        try:
            self.course1 = course1
            self.batch = batch
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
    def show(self):
        try:
            print("Course1 name = ",self.course1)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
    def display(self):
        try:
            print("Month of Batch started = ",self.batch)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
o = ineuron1("FSDS","May Batch")
o.display()
o.show()

class ineuron2:
    def __init__(self,course2):
        try:
            self.course2 = course2
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
    def display(self):
        try:
            print("Course2  namme = ",self.course2)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
o1 = ineuron2("FSDA")
o1.display()

class ineuron3:
    def __init__(self,course3):
        try:
            self.course3= course3
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
    def display(self):
        try:
            print("Course3 name = ",self.course3)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
o2 = ineuron3("FSWD")
o2.display()

class ineuron4:
    def __init__(self,course4):
        try:
            self.course4 = course4
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
    def display(self):
        try:
            print("Course4 name = ",self.course4)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")
o3 = ineuron4("NLP")
o3.display()

class ineuron5:
    def __init__(self,course5):
        try:
            self.course5 = course5
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

    def display(self):
        try:
            print("Course5 name = ",self.course5)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

o4 = ineuron4("CV")
o4.display()

class ineuron6:
    def __init__(self,course6):
        try:
            self.course6 = course6
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

    def display(self):
        try:
            print("Course6 name = ",self.course6)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

o5 = ineuron4("Deep Learning")
o5.display()

class ineuron7:
    def __init__(self,course7):
        try:
            self.course7 = course7
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

    def display(self):
        try:
            print("Course7 name = ",self.course7)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

o6 = ineuron7("Machine Learning")
o6.display()

class ineuron8:
    def __init__(self,course8):
        try:
            self.course8 = course8
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

    def display(self):
        try:
            print("Course8 name = ",self.course8)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

o7 = ineuron8("Statistic")
o7.display()

class ineuron9:
    def __init__(self,course9):
        try:
            self.course9 = course9
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

    def display(self):
        try:
            print("Course9 name = ",self.course9)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

o8= ineuron8("Big Data")
o8.display()

class ineuron10:
    def __init__(self,course10):
        try:
            self.course10 = course10
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

    def display(self):
        try:
            print("Course10 name = ",self.course10)
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")




# 10 examples on Polymorphism

class ineuron_students1:
    def students(self):
        try:
            print("print the students name which are enrolled for full stack data science course ")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students2:
    def students(self):
        try:
            print("print the students name who are enrolled for full stack web development course ")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students3:
    def students(self):
        try:
            print("print the students name who are enrolled for full stack data analytics course")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students3:
    def students(self):
        try:
            print("print the students name who are enrolled for Deep Leraning community class")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students4:
    def students(self):
        try:
            print("print the studenta name who are enrolled for machine learning community class")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students5:
    def students(self):
        try:
            print("print the name of students who are enrolled for NLP community class")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students6:
    def students(self):
        try:
            print("print the students name who are enrolled for statistics community class ")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students7:
    def students(self):
        try:
            print("print the students name who enrolled for cyber security classes")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students8:
    def students(self):
        try:
            print("print the students name who are enrolled for Javascript class ")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students9:
    def students(self):
        try:
            print("print the students name who are enrolled for BigData classes ")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class ineuron_students10:
    def students(self):
        try:
            print("print the students name who are enrolled for internship")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")


def ineuron_external(a):
    a.students()
O1 = ineuron_students1()
O2 = ineuron_students2()
O3 = ineuron_students3()
O4 = ineuron_students4()
O5 = ineuron_students5()
O6 = ineuron_students6()
O7 = ineuron_students7()
O8 = ineuron_students8()
O9 = ineuron_students9()
O10 = ineuron_students10()

ineuron_external(O1)
ineuron_external(O2)
ineuron_external(O3)
ineuron_external(O4)
ineuron_external(O5)
ineuron_external(O6)
ineuron_external(O7)
ineuron_external(O8)
ineuron_external(O9)
ineuron_external(O10)



# 10 examples on method overridding

class Courses1:
    def show(self):
        try:
            print("print the name of students who are enrolled for FSDS course")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class Courses2(Courses1):
    def show(self):
        try:
            print("print the name of students who are enrolled for FSDA  course")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

obj1 = Courses1()
obj2 = Courses2()
obj1.show()
obj2.show()
class Courses3:
    def show1(self):
        try:
            print("print the name of students who are enrolled for FSWD  course")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class Courses4(Courses3):
    def show1(self):
        try:
            print("print the students name from FSDS batch who has completed python project")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

obj3 = Courses3()
obj4 = Courses4()
obj3.show1()
obj4.show1()
class Courses5():
    def show2(self):
        try:
            print("print the name of students from FSDA batch who has completed time series project")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class Courses6(Courses5):
    def show2(self):
        try:
            print("print the name of students from FSWD batch who has completed project on E-Commerce")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

obj5 = Courses5()
obj6 = Courses6()
obj5.show2()
obj6.show2()
class Courses7:
    def show3(self):
        try:
            print("print the name of students from FSDS batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class Courses8(Courses7):
    def show3(self):
        try:
            print("print the name of students from FSDA batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

obj7 = Courses7()
obj8 = Courses8()
obj7.show3()
obj8.show3()
class Courses9:
    def show4(self):
        try:
            print("print the name of students from FSWD batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

class Courses10(Courses9):
    def show4(self):
        try:
            print("print the name of students from FSDS,FSDA,FSWD batches who got placed in the placement drive at ineuron.ai")
        except Exception as e:
            print(e)
            logging.debug("type error entered wrong argument ")

obj9 = Courses9()
obj10 = Courses10()
obj9.show4()
obj10.show4()
