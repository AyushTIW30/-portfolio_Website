from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is a home page")
    return render(request, "index.html")
def about(request):
    return HttpResponse("this is a about page")
def services(request):
    return HttpResponse("this is a services page")
def contact(request):
    return HttpResponse("this is a contact page")


