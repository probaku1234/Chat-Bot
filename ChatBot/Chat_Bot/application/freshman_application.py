from .student_application import student

class freshman(student):

    def show(self, message):
        return "whatever"

    def showRequiredDocuments(self):
        # keyword "Supporting Documents"
        return "document"

    def showApplicationProcess(self):
        # keyword "Apply Online"
        # keyword "Supporting Documents"
        return "application"

    # def showDeadlines(self):
    #     #FALL 2018
    #     #SPRING 2018
    #     return "deadline"

    # def showAdmissionCriteria(self):
    #     # keyword "Criteria"
    #     return "criteria"

    def getType(self):
        return "freshman"