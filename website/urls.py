from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
]
