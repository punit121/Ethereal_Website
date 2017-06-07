from django.conf.urls import include, url
from website.views import *
from . import views
app_name = 'website'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^services/$', views.services, name='services'),
    url(r'^product/$', views.product, name='product'),
    url(r'^store/$', views.store, name='store'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', register_success,name='register_success'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.view_profile, name='view_profile'),
    #url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/(?P<profile_id>[0-9]+)/$', views.edit_profile, name='edit_profile'),
    #url(r'^change-password/$', views.change_password, name='change_password'),

    #url(r'^reset-password/$', password_reset, {'template_name': 'website/reset_password.html', 'post_reset_redirect': 'website:password_reset_done', 'email_template_name': 'website/reset_password_email.html'}, name='reset_password'),

    #url(r'^reset-password/done/$', password_reset_done, {'template_name': 'website/reset_password_done.html'}, name='password_reset_done'),

    #url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'website/reset_password_confirm.html', 'post_reset_redirect': 'website:password_reset_complete'}, name='password_reset_confirm'),

    #url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'website/reset_password_complete.html'}, name='password_reset_complete')

]
