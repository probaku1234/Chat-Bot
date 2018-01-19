from .words_list import words_list
import requests
import re
from bs4 import BeautifulSoup


class application_Controller():

    student = None
    soup = None
    result = []
    homepage = "http://www.stonybrook.edu/"
    underg_admissions = "undergraduate-admissions/"
    apply = "apply/"
    application_procedures = "application-procedures/"
    text_content = None
    table_content = None
    url_content = None

    # CONSTRUCTOR
    # student_type SHOULD ONLY BE "freshman", "transfer" and "international"
    def __init__(self, student):
        self.setStudent(student)

    def setStudent(self, student):
        self.student = student
        self.setURL(student)
        self.setSoup()

    def setURL(self, student):
        self.url = self.homepage + self.underg_admissions + self.apply + \
                   student.getType() + "/" + self.application_procedures

    def setSoup(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.text, 'html.parser')
        self.text_content = self.parsing_text()
        self.table_content = self.parsing_table()
        self.url_content = self.parsing_url()

    def search(self, text):
        self.result.clear()
        text_result = self.find_text(text)
        isFound = False
        for element in text_result:
            if(self.getSibling(element)):
                isFound = True
            else:
                if(self.getParent(element)):
                    isFound = True

        if(not isFound):
            table_result = self.find_table(text)
            for element in table_result:
                if(self.getTableContent(element)):
                    isFound = True

        if(not isFound):
            url_result = self.find_url(text)
            for link in url_result:
                isFound = True
                self.result.append(link)

        if isFound:
            return self.prettify_result()
        else:
            return ""

    # get all text content
    def parsing_text(self):
        target_tag_names = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "b", "span", "strong"]
        return self.soup.find_all(target_tag_names)

    # look for all tags that match the text
    def find_text(self, keyword):
        matches = []
        print(keyword)
        for element in self.text_content:
            if (keyword in element.get_text()):
                matches.append(element)
        return matches

    # get all table content
    def parsing_table(self):
        return self.soup.find_all('table')

    # look for all tags that match the table
    def find_table(self, keyword):
        matches = []
        for table in self.table_content:
            # look for all tables that has text
            if (table.find(string=re.compile(keyword))):
                matches.append(table)
        return matches

    def parsing_url(self):
        target_tag_name = "a"
        return self.soup.find_all(target_tag_name)

    def find_url(self, keyword):
        matches = []
        for target_tag in self.url_content:
            if (keyword in target_tag.get_text()):
                matches.append(target_tag)
        return matches

    def getSibling(self, target_tag):
        isFound = False
        sibling = target_tag.find_next_sibling()
        if (sibling != None):
            if (sibling.name != "br"):
                self.result.append(target_tag)
                self.result.append(sibling)
                isFound = True
        return isFound

    def getParent(self, target_tag):
        isFound = False
        parent = target_tag.find_parent()
        if (parent != None):
            self.result.append(parent)
            isFound = True
        return isFound

    def getTableContent(self, target_tag):
        self.result.clear()
        th_tags = []
        rows = target_tag.find_all('tr')

        for row in rows:
            temp = row.find_all('th')
            if (temp != []):
                th_tags = temp
                break

        for row in rows:
            td_tags = row.find_all('td')
            th_tags_len = len(th_tags)
            td_tags_len = len(td_tags)
            if (th_tags_len > 0 and td_tags_len > 0):
                for i in range(0, th_tags_len):
                    self.result.append(th_tags[i])
                    self.result.append(td_tags[i])

    def prettify_result(self):
        message = ""
        for element in self.result:
            url_tag = element.find("a")
            if (url_tag != None):
                url = url_tag.get("href")
                if ("http" not in url):
                    url = self.homepage + url
                if (element.get_text() == url_tag.get_text()):
                    message += url_tag.get_text() + ": " + url
                else:
                    message += element.get_text() + url_tag.get_text() + ": " + url
            elif (element.name == "a"):
                url = element.get("href")
                if ("http" not in url):
                    url = self.homepage + url
                message += element.get_text() + ": " + url
            else:
                message += element.get_text()
                #if element.get_text()[-1] end with ":', then print......
                #print(element.get_text()[-1])
                #CASE: ADDITIONAL REQUIREMENTS
            message += "\n"
        print(message)
        return message

    #########################################################################################
    # TEST_CASE:
    #   "Supporting Documents" - entire div class (text)
    #   "High School Transcript" - sibling (text)
    #   "Deadline" - body table (table)
    #   "THE COMMON APPLICATION" - a href (url)
    #   "Social Work" - a href inside p (text and url)
    #   "Admission Criteria" - a class (url)
    #########################################################################################