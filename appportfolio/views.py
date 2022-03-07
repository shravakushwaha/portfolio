from django.shortcuts import render

# Create your views here.
def home(args):
    context = {}
    return render(args,'appportfolio/home.html')

def resume(request):
    context = {}
    return render(request, 'appportfolio/resume.html', context)

def experience(request):
    context = {}
    return render(request, 'appportfolio/experience.html', context)

