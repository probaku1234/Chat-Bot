from . import student, transfer, international, freshman

class apply():
    message = "What is your type of student? (transfer, international, freshman)"
    category = ""

    def createStudent(self, studentType):
        if (studentType == "transfer"):
            self.student = transfer.transfer()
        elif (studentType == "international"):
            self.student = international.international()
        elif (studentType == "freshman"):
            self.student = freshman.freshman()
        category = studentType

    # we need a method to recognize from user input -> our expected input
    def executeCommand(self, command):
        return self.student.show(command)
