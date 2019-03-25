from django.shortcuts import render
from django.utils import timezone
import datetime
# Create your views here.

def countdown(countdown):
        nu = datetime.datetime.now().__add__(-1)
        brexit = datetime.datetime.time(2019,3,29,23,0,0)
        countdown = datetime.time(brexit-nu)
        return countdown
