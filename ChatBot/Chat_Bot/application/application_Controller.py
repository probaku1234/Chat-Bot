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
    target_type = None
    target_relationship = None

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

    def search(self, text):
        self.target_type = None
        self.target_relationship = None
        self.result.clear()
        parsing_text_result = self.parsing_text(text)
        parsing_table_result = self.parsing_table(text)
        for element in parsing_text_result:
            self.getSibling(element)
            if (self.target_relationship == None):
                self.getParent(element)
        for element in parsing_table_result:
            self.getTableContent(element)
        if(len(parsing_text_result) == 0):
            parsing_url_result = self.parsing_url(text)
            for element in parsing_url_result:
                self.getURL(element)
        self.prettify_result()
        # need to return a string

    def parsing_text(self, text):
        target_tag_names = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "b", "span"]
        temp_list = []
        matches = []
        target_tags = self.soup.find_all(target_tag_names)
        temp_list.append(target_tags)

        # look for all tags that match the text
        for list in temp_list:
            for element in list:
                if (text in element.get_text()):
                    matches.append(element)
        return matches

    def parsing_url(self, text):
        target_tag_name = "a"
        matches = []
        target_tags = self.soup.find_all(target_tag_name)
        for target_tag in target_tags:
            if (text in target_tag.get_text()):
                matches.append(target_tag)
        return matches

    def parsing_table(self, text):
        matches = []
        tables = self.soup.find_all('table')
        for table in tables:
            # look for all tables that has text
            if (table.find(string=re.compile(text))):
                matches.append(table)
        return matches

    def getSibling(self, target_tag):
        sibling = target_tag.find_next_sibling()
        if (sibling != None):
            if (sibling.name != "br"):
                self.target_relationship = "has_sibling"
                self.result.append(target_tag)
                self.result.append(sibling)
            else:
                sibling = None
        return sibling

    def getParent(self, target_tag):
        parent = target_tag.find_parent()
        if (parent != None):
            self.target_relationship = "has_parent"
            self.result.append(parent)
        return parent

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

    def getURL(self, link):
        self.result.append(link)

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


    # TEST_CASE:
    #   "Supporting Documents" - entire div class (text)
    #   "High School Transcript" - sibling (text)
    #   "Deadline" - body table (table)
    #   "THE COMMON APPLICATION" - a href (url)
    #   "Social Work" - a href inside p (text and url)
    #   "Admission Criteria" - a class (url)

    ################################################################################################################
    def getMessage(self, keywords, student):

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
    #############################################################################################################