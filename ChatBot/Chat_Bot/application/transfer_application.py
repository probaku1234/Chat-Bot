from .student_application import student

class transfer(student):

    def show(self, message):
        return "whatever"

    def showRequiredDocuments(self):
        # keyword "sent"
        return "document"

    def showApplicationProcess(self):
        # keyword "Step"
        return "application"

    # def showDeadlines(self):
    #     #Fall 2018
    #     #Spring 2018
    #     return "deadline"

    # def showAdmissionCriteria(self):
    #     # keyword "Criteria"
    #     return "criteria"

    def getType(self):
        return "transfer"