from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class MyLoginView(LoginView):
    success_url = reverse_lazy('info')
    redirect_authenticated_user = True
    redirect_field_name = reverse_lazy('info')

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy('signup'))

class DeleteUser(generic.DeleteView):
    model = User
    success_url = reverse_lazy('info')

class ListUsers(generic.ListView):
    model = User
    success_url = reverse_lazy('info')
    template_name = 'assignment/user_list.html'