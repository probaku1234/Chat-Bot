from .student_application import student

class international(student):

    def show(self, message):
        return "whatever"

    def showRequiredDocuments(self):
        # keyword "upload"
        # keyword "English Proficiency"
        # keyword "Academic Records"
        return "document"

    def showApplicationProcess(self):
        # keyword "Step"
        return "application"

    # def showDeadlines(self):
    #     # FALL 2018 - Freshmen
    #     # FALL 2018 - Transfers
    #     # SPRING 2018
    #
    #     # SPRING 2018 - Freshmen
    #     # SPRING 2018 - Transfers
    #     # FALL 2019
    #     return "deadline"

    # def showAdmissionCriteria(self):
    #     # keyword "Criteria"
    #     return "criteria"

    def getType(self):
        return "international"