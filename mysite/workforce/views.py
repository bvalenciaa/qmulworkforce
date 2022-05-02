from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views import generic
from datetime import date

from .forms import *
from .decorators import *
from .models import *
from .filters import *


# LANDING PAGE

def landing(request):
    return render(request, 'workforce/landing.html')


# Register and Login Views - can only be used if user is unauthenticated

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)

            Member.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Welcome onboard ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'workforce/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')

    context = {}
    return render(request, 'workforce/login.html', context)


def logoutFunction(request):
    logout(request)
    return redirect('login')


# INDEX
# Index is the root location of the application, and loads the subsequent files

@login_required(login_url='login')
def index(request):
    team_id = request.user.member.team

    members = Member.objects.all()

    team_members = members.filter(team=team_id)

    context = {'team_members': team_members, 'members': members, 'team_id': team_id}
    return render(request, 'workforce/index.html', context)


def sidebar(request):
    team_id = request.user.member.team

    members = Member.objects.all()

    team_members = members.filter(team=team_id)

    context = {'team_members': team_members, 'members': members, 'team_id': team_id}
    return render(request, 'workforce/sidebar.html', context)


def userProfile(request):
    member = request.user.member
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'workforce/profile.html', context)


# HOME
# home contains all the individual information needed for the user

@login_required(login_url='login')
def home(request):
    # Creates a new task form
    form = TaskForm()
    member = request.user.member.id
    tasks = Task.objects.all()

    # creates new filter for the tasks
    member_tasks = tasks.filter(user=member)
    announcements = Announcement.objects.all()

    team_id = request.user.member.team
    members = Member.objects.all()
    team_members = members.filter(team=team_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')

    context = {'member': member, 'tasks': tasks, 'member_tasks': member_tasks, 'form': form,
               'announcements': announcements, 'team_members': team_members, 'members': members, 'team_id': team_id}
    return render(request, 'workforce/home.html', context)


# TASKS
# tasks encapsulate all the task information related to all users

def tasks(request):
    tasks = Task.objects.all()

    form = TaskForm()

    # task filter is created to sort through tasks
    myFilter = TaskFilter(request.GET, queryset=tasks)
    tasks = myFilter.qs

    team_id = request.user.member.team
    members = Member.objects.all()
    team_members = members.filter(team=team_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    context = {'tasks': tasks, 'form': form, 'myFilter': myFilter, 'team_members': team_members, 'members': members,
               'team_id': team_id}
    return render(request, 'workforce/tasks.html', context)


def editTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')

    context = {'form': form}
    return render(request, 'workforce/edit_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/tasks/')

    context = {'task': task}
    return render(request, 'workforce/delete_task.html', context)

# HUB
# hub contains all information relating to the team and deliverables

def hub(request):
    deliverables = Deliverables.objects.all()

    dev_count = deliverables.count()
    dev_bar = (100 / dev_count)

    teams = Team.objects.all()
    form = DeliverablesForm()

    team_id = request.user.member.team
    members = Member.objects.all()
    team_members = members.filter(team=team_id)

    if request.method == 'POST':
        form = DeliverablesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/hub/')
    context = {'deliverables': deliverables, 'dev_bar': dev_bar, 'teams': teams, 'form': form,
               'team_members': team_members, 'members': members, 'team_id': team_id}
    return render(request, 'workforce/hub.html', context)


def addTeam(request):
    form = addTeamForm()

    if request.method == 'POST':
        form = addTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'workforce/add_Team.html', context)


def editDeliverable(request, pk):
    deliverable = Deliverables.objects.get(id=pk)

    form = DeliverablesForm(instance=deliverable)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=deliverable)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'workforce/edit_deliverable.html', context)


def deleteDeliverable(request, pk):
    deliverable = Deliverables.objects.get(id=pk)

    if request.method == "POST":
        deliverable.delete()
        return redirect('/')

    context = {'deliverable': deliverable}
    return render(request, 'workforce/delete_deliverable.html', context)

# WORK
# work has all the work files relating to the project

def work(request):
    form = WorkForm()
    works = Work.objects.all()

    team_id = request.user.member.team
    members = Member.objects.all()
    team_members = members.filter(team=team_id)

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    context = {'form': form, 'works': works, 'team_members': team_members, 'members': members, 'team_id': team_id}
    return render(request, 'workforce/work.html', context)


def newWork(request):
    form = WorkForm()

    team_id = request.user.member.team
    members = Member.objects.all()
    team_members = members.filter(team=team_id)

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    context = {'form': form, 'team_members': team_members, 'members': members, 'team_id': team_id}
    return render(request, 'workforce/new_work.html', context)


def workDetail(request, pk):
    work = Work.objects.get(id=pk)
    context = {'work': work}
    return render(request, 'workforce/work_details.html', context)


def editWork(request, pk):
    work = Work.objects.get(id=pk)

    form = TaskForm(instance=work)

    if request.method == 'POST':
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('/work/')

    context = {'form': form}
    return render(request, 'workforce/edit_work.html', context)


def deleteWork(request, pk):
    work = Work.objects.get(id=pk)

    if request.method == "POST":
        work.delete()
        return redirect('/work/')

    context = {'work': work}
    return render(request, 'workforce/delete_work.html', context)

# MEDIA
# media contains all relevant media files

def media(request):
    uploads = Upload.objects.all()
    form = UploadFileForm()

    team_id = request.user.member.team
    members = Member.objects.all()
    team_members = members.filter(team=team_id)

    if request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'uploads': uploads, 'team_members': team_members, 'members': members, 'team_id': team_id}

    return render(request, 'workforce/media.html', context)


def editFile(request, pk):
    upload = Upload.objects.get(id=pk)

    form = UploadFileForm(instance=upload)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, instance=upload)
        if form.is_valid():
            form.save()
            return redirect('/media/')

    context = {'form': form}
    return render(request, 'workforce/edit_file.html', context)


def deleteFile(request, pk):
    upload = Upload.objects.get(id=pk)

    if request.method == "POST":
        upload.delete()
        return redirect('/media/')

    context = {'upload': upload}
    return render(request, 'workforce/delete_file.html', context)


def user(request):
    return render(request, 'workforce/user.html')
