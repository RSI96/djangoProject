from unicodedata import name
from django.urls import path
from website.views import home, about, date, story



urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('about/story/<str:pk>/', story, name='story'),
    path('date.html', date, name='date'),
]
