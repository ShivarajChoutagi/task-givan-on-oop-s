# 10 examples on public (3 example on 1st class, 3 example on 2nd class, 4 example on 3rd class)
import logging
logging.basicConfig(filename="inheritence.log",level=logging.DEBUG)
logging.debug('showing the debug error in givan object')
logging.info('shows error in givan class and object')
class ineuron1:
    def __init__(self):
        self.course1 = "FSDS"
    def course(self):
        try:
            print(self.course1)
            logging.debug("type error entered wrong argument ")
        except Exception as e:
            print(e)
o = ineuron1()
o.course()
o.course1="FSDA"
o.course()
o.course1="FSWD"
o.course()
o.course1 = "Community Classes"
o.course()


class ineuron2:
    def __init__(self):
        self.students1= "data science"

    def students(self):
        try:
            print(self.students1)
            logging.debug("type error entered wrong argument ")
        except Exception as e:
            print(e)
i = ineuron2()
i.students()
i.students1="data analytics"
i.students()
i.students1 = "web development"
i.students()
i.students1 = "Cyber Security"
i.students()

class ineuron3:
    def __init__(self):
        self.project1 = "Data Visualisation"
    def project(self):
        try:
            print(self.project1)
            logging.debug("type error entered wrong argument ")
        except Exception as e:
            print(e)
p = ineuron3()
p.project()
p.project1 = "E-commerce"
p.project()
p.project1 = "Object detection"
p.project()
p.project1 = "web scrapping"
p.project()
p.project1 = "time series"
p.project()