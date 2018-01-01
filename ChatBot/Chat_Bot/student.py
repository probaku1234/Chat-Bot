from abc import ABC, abstractmethod
from .words_list import words_list
import requests
import re
from bs4 import BeautifulSoup

class student(ABC):

    url_prefix = 'http://www.stonybrook.edu/undergraduate-admissions/apply/'
    url_suffix = '/application-procedures/'
    url = ''

    # student_type SHOULD ONLY BE "freshman", "transfer" and "international"
    def getMessage(self, keywords, student_type):
        self.url = self.url_prefix + student_type + self.url_suffix
        message = self.search(keywords)
        if(keywords == words_list.requiredDocs):
            self.showRequiredDocuments()
        elif(keywords == words_list.process):
            self.showApplicationProcess(message)
        elif(keywords == words_list.deadlines):
            self.showDeadlines()
        elif(keywords == words_list.criteria):
            self.showAdmissionCriteria()
        elif(keywords == words_list.contact):
            self.showContact(message)
        else:
            self.show(message)

    # METHOD TO TRAVERSE AND LOCATE THE CONTENT BY SEARCHING THE HTML
    # keyword: the keyword that we are looking for
    def search(self, keywords):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        target_html = soup.find_all("div")

        for element in target_html:
            result = []
            found_content = self.parseDiv(element, keywords, result)
            if (found_content != []):
                soup = BeautifulSoup(str(found_content), "html.parser")
                break

        #PROCESS WITH TEXTBLOB (ORGANIZE AND PRINT IT IN A READABLE WAY)
        message = "RESULT"
        return message

    # A RECURSIVE METHOD TO GET ALL PARENTS OF THE KEYWORD
    # div_content: the content to recurse
    # keyword: the keyword that we are looking for
    # result: A list of parents of the keyword
    def parseDiv(self, div_content, keyword, result):
        target_soup = BeautifulSoup(str(div_content), "html.parser")
        target_list = target_soup.find_all(text=re.compile(keyword))
        for target in target_list:
            if (target != None):
                result.append(target.find_parent("div"))
        return result

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

    def showContact(self):
        return "hello"

