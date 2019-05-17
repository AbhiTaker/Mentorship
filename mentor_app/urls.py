from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.index, name='index'),
    path('add_person/', views.add_person),
    path('assign_mentor/', views.assign_mentor),
    path('get_mentee/', views.get_mentee)
]