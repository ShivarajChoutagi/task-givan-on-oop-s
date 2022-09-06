import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)

logging.debug('showing the debug error in givan object')
logging.info('shows error in givan class and object')


class ineuron1:
    def __int__(self, student_name, enrolled_of_courses, affiliates, internship):
        self.student_name = student_name
        self.enrolled_of_courses = enrolled_of_courses
        self.affiliates = affiliates
        self.internship = internship


shivaraj = ineuron1("shivaraj", "fsds", "data_science", "not_done")
kumar = ineuron1("kumar", "fsda", "data_analytics", "doing")
student3 = ineuron1()
student4 = ineuron1()
student5 = ineuron1()

print(shivaraj.student_name)
print(kumar.student_name)
print(student3.student_name)
print(student4.student_name)
