from .student import student

class international(student):
    def showRequiredDocuments(self):
        return "document"

    def showApplicationProcess(self):
        return "application"

    def showDeadlines(self):
        return "deadline"

    def showAdmissionCriteria(self):
        return "criteria"