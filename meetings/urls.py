from unicodedata import name
from django.urls import path
from meetings.views import meetings, detail, add



urlpatterns = [
    path('', meetings, name='meetingsHome'),
    path('meeting/<int:id>', detail, name='detail'),
    path('add', add, name='add'),
]