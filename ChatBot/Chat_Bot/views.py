from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'Chat_Bot/index.html', {})

def processRequest(request):
    if (request.is_ajax()):
        return HttpResponse("hello!")
    else:
        raise Http404