from website.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import *


# Create your views here. 
def index(request):
	return render_to_response('website/index.html')

def about(request):
	return render_to_response('website/about.html')

def blog(request):
	return render_to_response('website/blog.html')

def contact(request):
	return render_to_response('website/contact.html')

def logout(request):
    logout(request)
    form = RegistrationForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'website/login.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                profile = Profile.objects.filter(user=request.user)
                return render(request, 'website/profile.html', {'profile': profile})
            else:
                return render(request, 'website/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'website/login.html', {'error_message': 'Invalid login'})
    return render(request, 'website/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    
 
    else:
        form = RegistrationForm()
    return render(request, 'website/reg_form.html', {'form': form})
def register_success(request):
    return render_to_response(
    'website/profile.html',
    )


            
"""
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'website/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('website/view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'website/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('website/view_profile'))
        else:
            return redirect(reverse('website/change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'website/change_password.html', args)					
"""        