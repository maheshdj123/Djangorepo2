from django.http import HttpResponse

# Create your views here.
def display(request):
    print("HI")
    s="<h1>Don't feel difficult...Just it is first time feeling....Really django is very easy....</h1>"
    return HttpResponse(s)
