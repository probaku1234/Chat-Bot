from . import student, transfer, international, freshman

class apply():
    message = "What is your type of student? (transfer, international, freshman)"

    def createStudent(self, studentType):
        if (studentType == "transfer"):
            self.student = transfer.transfer()
        elif (studentType == "international"):
            self.student = international.international()
        elif (studentType == "freshman"):
            self.student = freshman.freshman()

    def executeCommand(self, command):
        if (command == "documents"):
            return self.student.showRequiredDocuments()
        if (command == "application"):
            return self.student.showApplicationProcess()
        if (command == "deadlines"):
            return self.student.showDeadlines()
        if (command == "admission"):
            return self.student.showAdmissionCriteria()
