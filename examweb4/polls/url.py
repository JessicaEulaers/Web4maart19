from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('countdown', views.countdown, name='countdown'),

]