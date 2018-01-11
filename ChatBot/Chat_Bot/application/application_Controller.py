from .student_application import student
from .words_list import words_list
import requests
import re
from bs4 import BeautifulSoup


class application_Controller(student):

    url_prefix = 'http://www.stonybrook.edu/undergraduate-admissions/apply/'
    url_suffix = '/application-procedures/'
    url = ''

    # student_type SHOULD ONLY BE "freshman", "transfer" and "international"
    def getMessage(self, keywords, student):
        self.url = self.url_prefix + student.getType() + self.url_suffix
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
            parsedDiv_result = self.parseDiv(element, keywords, result)
            if (parsedDiv_result != []):
                soup = BeautifulSoup(str(parsedDiv_result), "html.parser")
                found_content = self.parseResult(result, keywords)
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

    def parseResult(self, result, keyword):
        isURL = False
        content = ""
        for element in result:
            soup = BeautifulSoup(str(element), "html.parser")
            a_string = soup.find_all("a")
            if (a_string != None):
                a_string_list = soup.select("div a")
                target_url = self.a_string_check(a_string_list, keyword)
                if (target_url != None):
                    content += target_url
                    isURL = True
            if (isURL == False):
                content += element.get_text()
        return content

    def a_string_check(self, a_string_list, keyword):
        target_url = None
        for link in a_string_list:
            if(link.string == keyword):
                target_url = link
                break
        return target_url