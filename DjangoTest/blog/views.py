from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def processRequest(request):
    if (request.is_ajax()):
        return HttpResponse("hello!")
    else:
        raise Http404