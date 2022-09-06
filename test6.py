import logging
logging.basicConfig(filename='test.log' , level=logging.DEBUG)

logging.debug('showing the debug error in givan object')
logging.info('shows error in givan class and object')
class ineuron_ai:
    def __init__(self):
        self.student='Shivaraj'
        self._course='data science'
        self.batch='fsds bootcamp'
        self.__email='shivaji@gmail.com'

    def students_info(self):
        logging.debug("enter right information otherwise gives error")
        try:
            print(self.student)
            print(self.batch)
            print(self._course)
            print(self.__email)

        except:
            logging.debug("type error plese enter right input")
            print('entered wrong information')



s=ineuron_ai()
s.students_info()
s.student='rajkumar'
s.student()
s._course='FSDS'
s._course()
s.__email='shivahi@ineuron.ai'
s.__email()
s.batch='fsds bootcamp'
s.batch()

