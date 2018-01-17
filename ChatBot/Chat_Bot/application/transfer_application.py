from .student_application import student

class transfer(student):

    def show(self):
        return "whatever"

    def showRequiredDocuments(self):
        # keyword "sent"
        return ["sent"]

    def showApplicationProcess(self):
        # keyword "Step"
        return ["Step"]

    # def showDeadlines(self):
    #     #Fall 2018
    #     #Spring 2018
    #     return "deadline"

    # def showAdmissionCriteria(self):
    #     # keyword "Criteria"
    #     return "criteria"

    def getType(self):
        return "transfer"