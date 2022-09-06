#  Examples on abstraction
import test8
print(test8)
obj2 = test8.ineuron3()
print(obj2.project())
import test7
print(test7)
obj1 = test7.Courses()
print(obj1.FSDS_course())
import test5
print(test5)
obj = test5.ineuron1("FSDA")
print(obj._ineuron1__course)
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
class ineuron2:
    logging.info("we are under ineuron2 class")
    def __init__(self,project,internship):
        logging.info("We are under the function of class ineuron2")
        try:
            self._project1 = project
            self.__internship1 = internship
        except Exception as e:
            logging.exception(e)
sonali = ineuron2("Object detection","doing internship from ineuron internship portal on BIG DATA")
print(sonali._project1)
print(sonali._ineuron2__internship1)


