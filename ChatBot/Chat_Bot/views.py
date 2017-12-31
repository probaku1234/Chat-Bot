from django.http import HttpResponse, Http404
from django.shortcuts import render
from textblob import TextBlob
from . import commandFactory

# Create your views here.
global command
global keywordList
global state

def post_list(request):
    global state
    state = 0
    return render(request, 'Chat_Bot/index.html', {})

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
            keywordList = TextBlob("documents application deadlines admission").words
            for word in textBlobSentence.words:
                for keyword in keywordList:
                    if (word == keyword):
                        return HttpResponse(command.executeCommand(word.string))
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