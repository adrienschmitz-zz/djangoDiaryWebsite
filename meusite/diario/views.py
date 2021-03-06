from django.shortcuts import render, get_object_or_404, redirect
import git
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Day
from django.utils import timezone
from .forms import DayForm


def day_list(request):
    return render(request, 'diario/day_list.html', {})


def day_list(request):
    days = Day.objects.filter(created_date__lte=timezone.now())
    return render(request, "diario/day_list.html", {"days": days})


def day_detail(request, pk):
    day = get_object_or_404(Day, pk=pk)
    return render(request, "diario/day_detail.html", {'day': day})


def day_new(request):
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            day = form.save(commit=False)
            day.author = request.user
            day.published_date = timezone.now()
            day.save()
            return redirect('day_detail', pk=day.pk)
    else:
        form = DayForm()
    return render(request, 'diario/day_edit.html', {'form': form})


def day_edit(request, pk):
    day = get_object_or_404(Day, pk=pk)
    if request.method == "POST":
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            day = form.save(commit=False)
            day.author = request.user
            day.published_date = timezone.now()
            day.save()
            return redirect('day_detail', pk=day.pk)
    else:
        form = DayForm(instance=day)
    return render(request, 'diario/day_edit.html', {'form': form})

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
