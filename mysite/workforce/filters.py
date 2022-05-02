import django_filters
from .models import *
from datetime import datetime
from calendar import HTMLCalendar


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['title', 'content', 'title']
