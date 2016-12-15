from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import ConnectForm, UserCreationForm

def home(request):
	return render(request, 'index.html');

def connect(request):
	error = False

	if request.method == "POST":
		form = ConnectForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
			else: # sinon une erreur sera affichée
				error = True
		page = redirect(reverse('home'));
	else:
		form = ConnectForm();
		page = render(request, 'connect.html', locals());

	return page;

def logout_view(request):
	logout(request);
	return redirect(reverse('home'))

def register(request):
	error = False

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
				login(request, user)  # nous connectons l'utilisateur
			else: # sinon une erreur sera affichée
				error = True
		page = redirect(reverse('home'));
	else:
		form = UserCreationForm();
		page = render(request, 'connect.html', locals());