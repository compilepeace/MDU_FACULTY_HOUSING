from django.shortcuts import render
from .models import Room,Status
# Create your views here.


def index(request):
    objs = Status.objects.all()
    rooms = [obj.room.number for obj in objs]
    status = [obj.status for obj in objs]
    context = dict(zip(rooms,status))
    # print(context)
    return render(request,'index.html',{'data':context})