import logging
logging.basicConfig(filename='test.log' , level=logging.DEBUG)

logging.debug('showing the debug error in givan object')
logging.info('shows error in givan class and object')
class ineuron1 :
    def student_name(self,student_name):
        print('take enroled student name is ',student_name)
        logging.debug('entered wrong name')
        return student_name

    def student_course(self,course_name):
        print('student enrolled to ',course_name)
        logging.debug('entered wrong course_name')
        return course_name
    def batch(self,batch_name):
        print('batch of course',batch_name)
        logging.debug('entered wrong batch_name')
        return batch_name

shiv=ineuron1()
raj=ineuron1()
renuji=ineuron1()

print(shiv.student_name("shivaraj"))
print(shiv.batch('fsds'))
print(shiv.student_course('FSDS cootcamp'))


