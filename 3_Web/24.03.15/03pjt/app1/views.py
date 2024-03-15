from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def about(request):
    return render(request, 'app1/profile.html')

def skill(request):
    return render(request, 'app1/skills.html')

def project(request):
    return render(request, 'app1/project.html')

def contact(request):
    return render(request, 'app1/contact.html')