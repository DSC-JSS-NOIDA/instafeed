from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.


# Admin Dashboard
def admin_page(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse_lazy('admin_login'))
	user = User.objects.get(id=request.user.id)
	details = Society.objects.get(society_user=user)
	return render(request, 'admin_page.html', {'society_details': details, 'username': user.username})




# Login Page
def admin_login(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = Login(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					return HttpResponseRedirect(reverse_lazy('admin_page'))
				else:
					return render(request, "admin_login.html", {"error": "Incorrect username or password!!!", 'form': form})
		else:
			form = Login()
		return render(request, "admin_login.html", {'form': form})
	else:
		return HttpResponseRedirect(reverse_lazy('admin_page'))



# Logout View
def admin_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse_lazy('admin_login'))



# Society Edit Page..........
def society_details(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse_lazy('admin_login'))
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		society = Society.objects.get(society_user=user)
		form = SocietyForm(request.POST, instance=society)
		print "Reached before checking validity!"
		if form.is_valid():
			form.save()
			print "Form Saved!!!!!"
		return HttpResponseRedirect(reverse_lazy('admin_page'))
	else:
		form = SocietyForm() 
	return render(request, 'society_details.html', {'form': form})
