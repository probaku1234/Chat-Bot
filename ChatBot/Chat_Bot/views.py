from django.http import HttpResponse, Http404
from django.shortcuts import render
from textblob import TextBlob
from . import commandFactory
from .application import words_list
from itertools import chain
from nltk.corpus import wordnet

# Create your views here.
global command
global keywordList
global state

def getSynlist(word):
    synonyms = wordnet.synsets(word)
    return set(chain.from_iterable([word.lemma_names() for word in synonyms]))

def post_list(request):
    global state
    state = 0
    return render(request, 'Chat_Bot/index.html', {})

def findMatchInList(sentence):
    sentence = sentence.lower()
    for word, pos in sentence.tags:
        if (pos == 'NN' or pos == "NNS"):
            print(word, pos)
            for keyword in words_list:
                if word in keyword._value_.lower():
                    return keyword._value_

                synset = getSynlist(word)
                print(synset)
                for syn in synset:
                    if syn in keyword._value_.lower():
                        return keyword._value_
            return None
    return None

def processRequest(request):
    if (request.is_ajax()):
        global command
        global keywordList
        global student
        global state

        message = request.GET.get("userMessage")

        textBlobSentence = TextBlob(message)
        if (state == 0):
            keywordList = TextBlob("transfer international freshman").words
            for word in textBlobSentence.words:
                for keyword in keywordList:
                    if (word == keyword):
                        state = 1
                        student = command.createStudent(word.string)
                        return HttpResponse("Ask question!")
            return HttpResponse("Please speak human language.")
        else:
            keyword = findMatchInList(textBlobSentence)
            if (keyword != None):
                return HttpResponse(command.executeCommand(keyword.string))
            else:
                return HttpResponse("Please speak human language.")
    else:
        raise Http404

def processSelection(requset):
    if (requset.is_ajax()):
        global command
        userSelect = requset.GET.get("userSelection")
        command = commandFactory.commandFactory().createCommand(userSelect)
        return HttpResponse(command.message)
    else:
        raise Http404