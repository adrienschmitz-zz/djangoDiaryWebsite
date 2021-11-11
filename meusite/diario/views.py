from django.shortcuts import render
import git
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Day
from django.utils import timezone


def day_list(request):
    return render(request, 'diario/day_list.html', {})


def day_list(request):
    days = Day.objects.filter(created_date__lte=timezone.now())
    return render(request, "diario/day_list.html", {"days": days})


# Git Webhook
@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("adrienschmitz.pythonanywhere.com/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
