from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from users.forms import UserAuthForm

from django.contrib import auth
from django.shortcuts import render

from users.forms import UserAuthForm


def auth_user(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserAuthForm()

    context = {'form': form}
    return render(request, 'users/auth.html', context)


def register(request):
    return render(request, 'users/registration.html')
