from .application import international_application, transfer_application, freshman_application
from .application import application_Controller

class apply():
    message = "What is your type of student? (transfer, international, freshman)"
    category = ""

    def createStudent(self, studentType):
        if (studentType == "transfer"):
            self.student = transfer_application.transfer()
        elif (studentType == "international"):
            self.student = international_application.international()
        elif (studentType == "freshman"):
            self.student = freshman_application.freshman()
        self.controller = application_Controller.application_Controller(self.student)
        self.category = studentType

    # we need a method to recognize from user input -> our expected input
    #def executeCommand(self, command):
    #    return self.student.show(command)

    def executeCommand(self, command):
        self.controller.getMessage(command, self.student)
