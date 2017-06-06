from website.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy, resolve
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Profile

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
# Create your views here. 
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'website/index.html')
    else:
        user = request.user
        #profile = get_object_or_404(Profile, pk=album_id)
        return render(request, 'website/index.html', {'user': user})
#	return render_to_response('website/index.html')

def about(request):
    if not request.user.is_authenticated():
        return render(request, 'website/about.html')
    else:
        user = request.user
        #profile = get_object_or_404(Profile, pk=album_id)
        return render(request, 'website/about.html', {'user': user})
#	return render_to_response('website/about.html')

def blog(request):
    if not request.user.is_authenticated():
        return render(request, 'website/blog.html')
    else:
        user = request.user
        #profile = get_object_or_404(Profile, pk=album_id)
        return render(request, 'website/blog.html', {'user': user})
#	return render_to_response('website/blog.html')

def contact(request):
    if not request.user.is_authenticated():
        return render(request, 'website/contact.html')
    else:
        user = request.user
        #profile = get_object_or_404(Profile, pk=album_id)
        return render(request, 'website/contact.html', {'user': user})
#	return render_to_response('website/contact.html')

def logout_user(request):
    logout(request)
    form = RegistrationForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'website/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
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
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        #form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    profile = Profile.objects.filter(user=request.user)
                    return render(request, 'website/profile.html', {'profile': profile})
    context = {
        "form": form,
    }
    return render(request, 'website/reg_form.html', context)
    

def register_success(request):
    return render_to_response(
    'website/profile.html',
    )

def view_profile(request,profile_id):
    if not request.user.is_authenticated():
        return render(request, 'website/index.html')
    else:
        user = request.user
        profile = Profile.objects.filter(user=request.user)
        return render(request, 'website/profile.html', {'profile': profile} )
#@login_required
def edit_profile(request,profile_id):
    #profile = get_object_or_404(Profile,pk=user_id)
    #context = {'profile': profile}
    form = EditProfileForm(request.POST or None, request.FILES or None,instance=request.user.profile)
    #args={}
    if request.method == 'POST':
        if form.is_valid():        
            profile = form.save(commit=False)
            profile.user = request.user
            profile.image = request.FILES['image']
            #file_type = form.image.url.split('.')[-1]
            #file_type = file_type.lower()
            #if file_type not in IMAGE_FILE_TYPES:
            #        context = {
            #            'profile': profile,
            #            'form': form,
            #            'error_message': 'Image file must be PNG, JPG, or JPEG',
            #        }
            #        return render(request, 'website/edit_profile.html', context)
            profile.save()
            profile = Profile.objects.filter(user=request.user)
            return render(request, 'website/profile.html', {'profile': profile})
    context = {
        "form": form,
    }
    return render(request, 'website/edit_profile.html', context)

    
            
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