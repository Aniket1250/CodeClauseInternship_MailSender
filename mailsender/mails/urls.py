from django.urls import path
from mails import views

urlpatterns = [
    path('login',views.login_page,name='login'),
    path('register',views.register_page,name='register'),
    path('',views.home,name='home'),
    path('logout',views.logout_page,name='logout'),
    path('mails',views.mails,name='mails'),
]