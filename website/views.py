from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
	return render_to_response('website/index.html')

def about(request):
	return render_to_response('website/about.html')

def blog(request):
	return render_to_response('website/blog.html')

def contact(request):
	return render_to_response('website/contact.html')

def login(request):
	return render_to_response('website/login.html')

def register(request):
	return render_to_response('website/register.html')					