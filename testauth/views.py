import imp
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from testauth.models import Dashboard
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class Dash(LoginRequiredMixin, ListView):
    model = Dashboard


class CustomLoginView(LoginView):
    template_name: 'testauth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 
    def get_success_url(self):
        return reverse_lazy('authtest')


class RegisterPage(FormView):
    template_name: 'testauth/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True 
    success_url = reverse_lazy('authtest')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('authtest')
        return super(RegisterPage, self).get(*args, **kwargs)

