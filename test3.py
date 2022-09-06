import logging
logging.basicConfig(filename='test.log' , level=logging.DEBUG)

logging.debug('showing the debug error in givan object')
logging.info('shows error in givan class and object')
class ineuron2:

    def __init__(self,name, course, batch, internship):
        self.name = name
        self.course = course
        self.batch = batch
        self.internship = internship

anuj_var = ineuron2('anuj_raj','fsds','fsds bootcamp','notdone')
shiv=ineuron2('shivaraj','mldl','deeplearning',"doing")
gadagi=ineuron2('gahadhigayya','fsda','data analytics','done')

print(anuj_var.name)
print(shiv.name)
print(gadagi.name)
print(type(shiv))