from django.shortcuts import render
from .models import Room,Status
# Create your views here.


def index(request):
    objs = Status.objects.all()
    ts_objs = Room.objects.order_by('updated_on')
    list_objs = list(ts_objs)
    time = list_objs[-1].updated_on
    #timestamp = [ts_obj.updated_on for ts_obj in ts_objs ]
    rooms = [obj.room.number for obj in objs]
    status = [obj.status for obj in objs]
    context = dict(zip(rooms, status))
    #ts_dict = dict(zip(rooms, timestamp))
    # print(context)
    return render(request,'index.html',{'data':context, 'timestamp': time})