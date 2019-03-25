from django.shortcuts import render
from django.utils.timezone import localtime, now
import datetime
# Create your views here.
def index(request):
        now = localtime(now);
        brexit = datetime.datetime.time(2019,3,29)
        return render(request, 'polls/index.html', {'movie_name': movieslist})
