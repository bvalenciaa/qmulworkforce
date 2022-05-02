from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user', 'team']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'


class DeliverablesForm(forms.ModelForm):
    class Meta:
        model = Deliverables
        fields = '__all__'


class addTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class NewAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'
        exclude = ['user']

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        exclude = ['created']
