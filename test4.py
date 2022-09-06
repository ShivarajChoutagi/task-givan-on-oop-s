import logging
logging.basicConfig(filename='test.log' , level=logging.DEBUG)

logging.debug('showing the debug error in givan object')
logging.info('shows error in givan class and object')
class ineuron:
    def student(self,student_full_name):
        return student_full_name
    def email_id_input(self,email_id):
        print('take mauil from person and print it',email_id)

    def ask_course(self):
        course=input('ask for course')
        return course
    def batch_name(self):
        batch_name=input('enter the batch_name')
        return batch_name

shiv=ineuron()
raj=ineuron()
ravi=ineuron()
randi=ineuron()

shiv.email_id_input('shivajiychouttagi@gmail')
print(shiv.batch_name())
print(raj.ask_course())
