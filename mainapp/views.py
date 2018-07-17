# chat/views.py
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import Room
import json
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    userid = request.user.username;
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'userid': userid,
    })


@login_required
def page(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    return render(request, "index.html", {
        "rooms": rooms
    })


"""
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
"""


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


