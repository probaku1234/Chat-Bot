from .student_application import student

class freshman(student):

    def show(self):
        return "whatever"

    def showRequiredDocuments(self):
        return ["Supporting Documents"]

    def showApplicationProcess(self):
        return ["Apply Online", "Supporting Documents"]

    # def showDeadlines(self):
    #     #FALL 2018
    #     #SPRING 2018
    #     return "deadline"

    # def showAdmissionCriteria(self):
    #     # keyword "Criteria"
    #     return "criteria"

    def getType(self):
        return "freshman"