from unicodedata import name
from django.urls import path
from .views import CustomLoginView, Dash,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',CustomLoginView.as_view() , name='login'),
    path('logout/',LogoutView.as_view(next_page='login') , name='logout'),
    path('register/',RegisterPage.as_view(template_name='testauth/register.html'), name='register'),

    path('',Dash.as_view() , name='authtest'),
    

]