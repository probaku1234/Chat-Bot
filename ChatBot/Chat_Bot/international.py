from .student import student

class international(student):

    def show(self, message):
        return "whatever"

    def showRequiredDocuments(self):
        return "document"

    def showApplicationProcess(self):
        return "application"

    def showDeadlines(self):
        return "deadline"

    def showAdmissionCriteria(self):
        return "criteria"