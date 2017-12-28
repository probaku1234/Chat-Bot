from django.http import HttpResponse, Http404
from django.shortcuts import render
from textblob import TextBlob

# Create your views here.
def post_list(request):
    return render(request, 'Chat_Bot/index.html', {})

def processRequest(request):
    if (request.is_ajax()):
        message = request.GET.get("userMessage")
        selection = request.GET.get("userSelect")
        textBlobSentence = TextBlob(message)
        print(message)
        return HttpResponse("hello!")
    else:
        raise Http404