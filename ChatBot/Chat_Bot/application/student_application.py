from abc import ABC, abstractmethod

class student(ABC):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def showRequiredDocuments(self):
        pass

    @abstractmethod
    def showApplicationProcess(self):
        pass

    def showDeadlines(self):
        return ["Deadline"]

    def showAdmissionCriteria(self):
        return ["Criteria"]

    @abstractmethod
    def getType(self):
        pass

    def showContact(self):
        return ["hello"]

