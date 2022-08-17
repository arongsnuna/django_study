from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from .forms import RoomForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    paginator = Paginator(rooms, 3)
    pagnum = request.GET.get('page')
    rooms = paginator.get_page(pagnum)
    return render(request, 'home.html', {'rooms':rooms})

def roomcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    return render(request, 'room_form.html', {'form':form})

def detail(request, room_id):
    room_detail = get_object_or_404(Room, pk=room_id)
    return render(request, 'detail.html', {'room_detail':room_detail})