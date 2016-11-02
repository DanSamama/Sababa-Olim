from django.shortcuts import render
from django.views import generic
from .models import Message
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def check_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("Us1er is valid, active and authenticated")
            login(request, user)
            return HttpResponseRedirect('/sababa/')
    else:
        print("The password is valid, but the account has been disabled!")
        form = UserCreationForm()
        return render(request, "registration/register.html", {
            'form': form,
        })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)

            login(request, new_user)
            return HttpResponseRedirect("/sababa/")
        else:
            form = UserCreationForm()
            return render(request, "registration/register.html", {
                'form': form,
            })
    else:
        form = UserCreationForm()
        return render(request, "registration/register.html", {
            'form': form,
        })
