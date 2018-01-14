from abc import ABC, abstractmethod

class student(ABC):

    @abstractmethod
    def show(self, keywords):
        pass

    @abstractmethod
    def showRequiredDocuments(self):
        pass

    @abstractmethod
    def showApplicationProcess(self):
        pass

    def showDeadlines(self):
        # keyword "Deadline"
        return "Deadline"

    def showAdmissionCriteria(self):
        # keyword "Criteria"
        return "Criteria"

    @abstractmethod
    def getType(self):
        pass

    def showContact(self):
        return "hello"

