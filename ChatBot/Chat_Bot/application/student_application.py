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

    @abstractmethod
    def showDeadlines(self):
        pass

    @abstractmethod
    def showAdmissionCriteria(self):
        pass

    @abstractmethod
    def getType(self):
        pass

    def showContact(self):
        return "hello"

